
import pandas as pd
import numpy as np
from scipy.stats import poisson
import glob

print("--- INICIANDO MOTOR POISSON AUTOMATIZADO ---")

# 1. Escanea tu repositorio buscando cualquier CSV
archivos_csv = glob.glob('*.csv')

if not archivos_csv:
    print("❌ No se encontraron archivos CSV. Abortando misión.")
    exit()

print(f"Archivos detectados para auditar: {archivos_csv}")

ligas_procesadas = {}

# 2. Procesamiento masivo
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    
    # Checamos si es un archivo de resultados válido
    if 'FTHG' not in df.columns or 'FTAG' not in df.columns:
        print(f"⚠️ Saltando {archivo}: No trae el formato de resultados.")
        continue
        
    df = df.rename(columns={'FTHG': 'goles_reales_local', 'FTAG': 'goles_reales_visitante'})
    
    # MATEMÁTICA BASE
    promedio_goles_local_liga = df['goles_reales_local'].mean()
    promedio_goles_visitante_liga = df['goles_reales_visitante'].mean()
    
    stats_local = df.groupby('HomeTeam').agg({'goles_reales_local': 'mean', 'goles_reales_visitante': 'mean'}).rename(columns={'goles_reales_local': 'goles_anotados_local', 'goles_reales_visitante': 'goles_recibidos_local'})
    stats_visitante = df.groupby('AwayTeam').agg({'goles_reales_visitante': 'mean', 'goles_reales_local': 'mean'}).rename(columns={'goles_reales_visitante': 'goles_anotados_visitante', 'goles_reales_local': 'goles_recibidos_visitante'})
    
    stats_local['fuerza_ataque_local'] = stats_local['goles_anotados_local'] / promedio_goles_local_liga
    stats_local['fuerza_defensa_local'] = stats_local['goles_recibidos_local'] / promedio_goles_visitante_liga
    stats_visitante['fuerza_ataque_visitante'] = stats_visitante['goles_anotados_visitante'] / promedio_goles_visitante_liga
    stats_visitante['fuerza_defensa_visitante'] = stats_visitante['goles_recibidos_visitante'] / promedio_goles_local_liga
    
    df = df.merge(stats_local[['fuerza_ataque_local', 'fuerza_defensa_local']], left_on='HomeTeam', right_index=True)
    df = df.merge(stats_visitante[['fuerza_ataque_visitante', 'fuerza_defensa_visitante']], left_on='AwayTeam', right_index=True)
    
    df['xg_local'] = df['fuerza_ataque_local'] * df['fuerza_defensa_visitante'] * promedio_goles_local_liga
    df['xg_visitante'] = df['fuerza_ataque_visitante'] * df['fuerza_defensa_local'] * promedio_goles_visitante_liga
    
    # DETECCIÓN DE VALOR Y KELLY
    if 'B365H' in df.columns: cols = ['B365H', 'B365D', 'B365A']
    elif 'PSH' in df.columns: cols = ['PSH', 'PSD', 'PSA']
    elif 'AvgH' in df.columns: cols = ['AvgH', 'AvgD', 'AvgA']
    elif 'BVCH' in df.columns: cols = ['BVCH', 'BVCD', 'BVCA']
    else: continue
        
    df = df.dropna(subset=cols)
    
    prob_local = []
    for index, row in df.iterrows():
        xg_l, xg_v = row['xg_local'], row['xg_visitante']
        p_l = sum(poisson.pmf(gl, xg_l) * poisson.pmf(gv, xg_v) for gl in range(6) for gv in range(6) if gl > gv)
        prob_local.append(p_l)
        
    df['prob_modelo_local'] = prob_local
    df['prob_casino_local'] = 1 / df[cols[0]]
    df['hay_valor_local'] = df['prob_modelo_local'] > df['prob_casino_local']
    df['kelly_local'] = ((df['prob_modelo_local'] * df[cols[0]]) - 1) / (df[cols[0]] - 1)
    
    # Tope del 5% del bankroll
    df['apuesta_sugerida'] = np.where((df['hay_valor_local']) & (df['kelly_local'] > 0), df['kelly_local'], 0)
    df['apuesta_sugerida'] = np.clip(df['apuesta_sugerida'], 0, 0.05)
    
    df['ganancia_apuesta'] = np.where(df['goles_reales_local'] > df['goles_reales_visitante'], df['apuesta_sugerida'] * (df[cols[0]] - 1), -df['apuesta_sugerida'])
    
    ligas_procesadas[archivo] = df
    unidades = df['ganancia_apuesta'].sum() * 100
    print(f"✅ {archivo}: {unidades:.2f} ud generadas en la simulación.")

# 3. Guardado Maestro
print("\n--- EMPAQUETANDO RESULTADOS ---")
if ligas_procesadas:
    df_final = pd.concat(ligas_procesadas.values(), ignore_index=True)
    df_final.to_csv('reporte_maestro_kelly.csv', index=False)
    print("💾 Archivo 'reporte_maestro_kelly.csv' guardado con éxito. ¡Listo para cobrar!")
