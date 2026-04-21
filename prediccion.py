import os
import time
from datetime import datetime
import pandas as pd
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    # 1. ¿Qué día es hoy?
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    print(f"Buscando partidos para hoy: {fecha_hoy}")
    
    # Tus carpetas / archivos en GitHub
    archivos_masivos = {
        "La Liga": "Laliga2326.csv",
        "Premier League": "Premier2326.csv",
        "Serie A": "SerieA2326.csv",
        "Bundesliga": "Bundesliga2326.csv"
    }
    
    contexto_para_ia = ""
    partidos_encontrados = False
    
    # 2. El Filtro Inteligente (Cruzar Información)
    for liga, archivo in archivos_masivos.items():
        try:
            df = pd.read_csv(archivo, low_memory=False)
            partidos_hoy = df[df['Date'] == fecha_hoy]
            
            if not partidos_hoy.empty:
                partidos_encontrados = True
                contexto_para_ia += f"\n\n--- 🏆 {liga.upper()} (HOY) ---\n"
                
                for _, partido in partidos_hoy.iterrows():
                    local = partido['HomeTeam']
                    visitante = partido['AwayTeam']
                    
                    # Cruzamos datos: Buscamos los últimos 5 partidos históricos SOLO de estos dos equipos
                    historial_local = df[(df['HomeTeam'] == local) | (df['AwayTeam'] == local)].tail(5)
                    historial_visitante = df[(df['HomeTeam'] == visitante) | (df['AwayTeam'] == visitante)].tail(5)
                    
                    contexto_para_ia += f"⚽ ENCUENTRO: {local} (Local) vs {visitante} (Visitante)\n"
                    contexto_para_ia += f"- Últimos 5 juegos de {local} (Goles a favor/contra): \n{historial_local[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    contexto_para_ia += f"- Últimos 5 juegos de {visitante} (Goles a favor/contra): \n{historial_visitante[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")

    # 3. Si no hay partidos hoy, frenamos para no gastar recursos
    if not partidos_encontrados:
        print("No hay encuentros programados para hoy. Finalizando.")
        with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
            archivo.write(f"# 🏆 Análisis Diario Automatizado\n\n**Fecha:** {fecha_hoy}\n\nNo hay encuentros programados en las bases de datos para el día de hoy.")
        return

    # 4. El Prompt Minimalista (Evita saturar el servidor)
    prompt = f"""
    Actúa como un analista cuantitativo deportivo. Hoy es {fecha_hoy}.
    
    Aquí tienes los datos cruzados (historial reciente) estrictamente de los equipos que juegan HOY:
    {contexto_para_ia}
    
    INSTRUCCIONES:
    1. Usa tu herramienta de BÚSQUEDA EN GOOGLE para investigar el estado actual de estos equipos específicos (noticias de última hora de hoy, lesiones importantes, bajas, suspensiones).
    2. Aplica la distribución de Poisson sobre los goles recientes que te acabo de proporcionar para calcular la proyección ofensiva (xG).
    3. Basado en los números y las noticias en vivo, dame el pronóstico de valor (CLV) para cada encuentro.
    4. Sugiere el tamaño de inversión usando el Criterio de Kelly.
    """
    
    print("Iniciando IA con búsqueda en Internet y datos cruzados...")
    
    # 5. Conexión Antisaturación
    max_reintentos = 3
    for intento in range(max_reintentos):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[{"google_search": {}}] # <--- Se le da acceso a Internet a la IA
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
        archivo.write(f"# 📊 Análisis Diario: {fecha_hoy}\n\n")
        archivo.write(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
