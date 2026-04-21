import os
import time
import pandas as pd
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    # Tus 4 archivos unificados con el historial completo
    archivos_masivos = {
        "La Liga": "Laliga2326.csv",
        "Premier League": "Premier2326.csv",
        "Serie A": "SerieA2326.csv",
        "Bundesliga": "Bundesliga2326.csv"
    }
    
    resumen_global = ""
    
    for liga, archivo in archivos_masivos.items():
        try:
            df = pd.read_csv(archivo, low_memory=False)
            # Extraemos los últimos 10 partidos para el contexto inmediato
            ultimos = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].tail(10).to_string(index=False)
            resumen_global += f"\n--- {liga.upper()} (HISTORIAL COMPLETO 23-26) ---\n{ultimos}\n"
        except Exception as e:
            resumen_global += f"\nNo se pudo leer {archivo} en {liga}. Revisa que el nombre sea exacto: {e}\n"

    prompt = f"""
    Actúa como un analista cuantitativo experto. Tienes acceso a una base de datos histórica masiva de las 4 grandes ligas europeas (Temporadas 2023 a 2026).
    
    Basado en el contexto de estos resultados recientes extraídos de la base de datos:
    {resumen_global}
    
    Usando principios de Sabermetrics, distribución de Poisson y xG (goles esperados) calculados sobre este volumen de datos:
    1. Identifica las anomalías o tendencias más fuertes en el rendimiento ofensivo/defensivo por liga.
    2. Sugiere los pronósticos de mayor valor (Closing Line Value) en toda Europa.
    3. Recomienda exactamente cómo estructurar el tamaño de la inversión usando el Criterio de Kelly.
    """
    
    print("Iniciando motor de predicción cuantitativo (4 archivos maestros)...")
    
    max_reintentos = 3
    for intento in range(max_reintentos):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            break
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"⚠️ Servidor saturado (Intento {intento + 1}/{max_reintentos}). Esperando 20 segundos...")
                time.sleep(20)
                if intento == max_reintentos - 1:
                    print("❌ El servidor sigue saturado. Intenta correr más tarde.")
                    return
            else:
                print(f"❌ Error inesperado: {e}")
                return
    
    print("\nGuardando el reporte en REPORTE_EUROPEO.md...")
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write("# 🏆 Análisis Cuantitativo Masivo: Europa (Temporadas 23-26)\n\n")
        archivo.write(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
