import os
import time # Importante: Nos permite poner el código en pausa
import pandas as pd
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    ligas = [
        'premier_league_2526.csv', 
        'la_liga_2526.csv', 
        'serie_a_2526.csv', 
        'bundesliga_2526.csv'
    ]
    
    resumen_datos = ""
    
    for liga in ligas:
        try:
            df = pd.read_csv(liga)
            ultimos = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].tail(5).to_string(index=False)
            resumen_datos += f"\n--- LIGA: {liga} ---\n{ultimos}\n"
        except Exception as e:
            resumen_datos += f"\nNo se pudo leer {liga}. Error: {e}\n"
            
    prompt = f"""
    Actúa como un analista cuantitativo experto. Usando principios de Sabermetrics, la distribución de Poisson, aproximaciones de xG (goles esperados) y el Criterio de Kelly, analiza los siguientes resultados recientes:
    
    {resumen_datos}
    
    Evalúa el rendimiento (FTHG = Goles Local, FTAG = Goles Visitante). 
    1. Calcula qué equipos muestran la mejor proyección ofensiva actual.
    2. Sugiere 2 pronósticos de valor (CLV) para los próximos encuentros de estas ligas.
    3. Recomienda cómo estructurar el tamaño de la inversión usando el Criterio de Kelly.
    """
    
    print("Iniciando motor de predicción europeo con el nuevo SDK...")
    
    # --- SISTEMA DE REINTENTO (ANTISATURACIÓN) ---
    max_reintentos = 3
    
    for intento in range(max_reintentos):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            break # Si la IA responde bien, salimos de este bucle de reintentos
            
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"⚠️ Servidor de Google saturado (Intento {intento + 1}/{max_reintentos}). Esperando 20 segundos...")
                time.sleep(20) # Pausa el script 20 segundos antes de volver a intentar
                if intento == max_reintentos - 1:
                    print("❌ El servidor sigue saturado después de 3 intentos. Intenta correr la acción más tarde.")
                    return
            else:
                print(f"❌ Error inesperado de la API: {e}")
                return
    
    # Mostrar resultados
    print("\n" + "="*40)
    print("🏆 PREDICCIONES EUROPEAS GENERADAS 🏆")
    print("="*40)
    print(response.text)

    # Guardar documento
    print("\nGuardando el reporte en REPORTE_EUROPEO.md...")
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write("# 🏆 Análisis Cuantitativo Europeo\n\n")
        archivo.write(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
