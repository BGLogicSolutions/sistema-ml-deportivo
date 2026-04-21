import os
import time
from datetime import datetime, timedelta, timezone
import pandas as pd
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    # 1. Ajustar el reloj del servidor para que "hoy" coincida con tu zona horaria (UTC-6)
    zona_horaria = timezone(timedelta(hours=-6))
    hoy = datetime.now(zona_horaria).date()
    fecha_str = hoy.strftime("%d/%m/%Y")
    print(f"Sincronizando calendario. Buscando partidos para hoy: {fecha_str}")
    
    archivos_masivos = {
        "La Liga": "Laliga2326.csv",
        "Premier League": "Premier2326.csv",
        "Serie A": "SerieA2326.csv",
        "Bundesliga": "Bundesliga2326.csv"
    }
    
    contexto_para_ia = ""
    partidos_encontrados = False
    
    # 2. El Filtro Inteligente y Limpieza de Fechas
    for liga, archivo in archivos_masivos.items():
        try:
            df = pd.read_csv(archivo, low_memory=False)
            
            # MAGIA AQUÍ: Obliga a Python a entender cualquier formato de fecha y estandarizarlo
            df['Fecha_Limpia'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce').dt.date
            
            # Filtramos los partidos usando la fecha ya limpia
            partidos_hoy = df[df['Fecha_Limpia'] == hoy]
            
            if not partidos_hoy.empty:
                partidos_encontrados = True
                contexto_para_ia += f"\n\n--- 🏆 {liga.upper()} (HOY) ---\n"
                
                for _, partido in partidos_hoy.iterrows():
                    local = partido['HomeTeam']
                    visitante = partido['AwayTeam']
                    
                    historial_local = df[(df['HomeTeam'] == local) | (df['AwayTeam'] == local)].tail(5)
                    historial_visitante = df[(df['HomeTeam'] == visitante) | (df['AwayTeam'] == visitante)].tail(5)
                    
                    contexto_para_ia += f"⚽ ENCUENTRO: {local} vs {visitante}\n"
                    contexto_para_ia += f"- Últimos 5 de {local}: \n{historial_local[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    contexto_para_ia += f"- Últimos 5 de {visitante}: \n{historial_visitante[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")

    if not partidos_encontrados:
        print("No se encontraron partidos programados en los archivos CSV.")
        with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
            archivo.write(f"# 🏆 Análisis Diario Automatizado\n\n**Fecha:** {fecha_str}\n\nLos archivos CSV no contienen encuentros programados para el día de hoy.")
        return

    prompt = f"""
    Actúa como un analista cuantitativo deportivo. Hoy es {fecha_str}.
    
    Aquí tienes el historial cruzado estrictamente de los equipos de las ligas principales que juegan HOY:
    {contexto_para_ia}
    
    INSTRUCCIONES:
    1. Usa tu herramienta de BÚSQUEDA EN GOOGLE para investigar el estado en tiempo real de estos equipos (noticias de última hora, lesiones críticas, alineaciones confirmadas).
    2. Aplica la distribución de Poisson sobre los goles históricos proporcionados para aproximar el xG.
    3. Combina los datos duros con las noticias en vivo para encontrar el mayor valor (CLV).
    4. Sugiere el porcentaje de inversión usando el Criterio de Kelly.
    """
    
    print("Iniciando IA con búsqueda en Internet y datos cruzados...")
    
    max_reintentos = 3
    for intento in range(max_reintentos):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[{"google_search": {}}]
                )
            )
            break
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"⚠️ Servidor ocupado (Intento {intento + 1}/3). Pausando 20 seg...")
                time.sleep(20)
                if intento == max_reintentos - 1:
                    print("❌ Servidor saturado.")
                    return
            else:
                print(f"❌ Error: {e}")
                return
    
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write(f"# 📊 Análisis Diario: {fecha_str}\n\n")
        archivo.write(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
