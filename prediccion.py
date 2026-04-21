import os
import pandas as pd
import google.generativeai as genai

# Conexión con tu llave secreta y la versión correcta del modelo
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = model = genai.GenerativeModel('gemini-pro')


def ejecutar_analisis():
    # Lista exacta de los archivos que acabas de subir
    ligas = [
        'premier_league_2526.csv', 
        'la_liga_2526.csv', 
        'serie_a_2526.csv', 
        'bundesliga_2526.csv'
    ]
    
    resumen_datos = ""
    
    # Leemos los últimos 5 partidos de cada liga
    for liga in ligas:
        try:
            df = pd.read_csv(liga)
            # Extraemos: Fecha, Local, Visitante, Goles Local (FTHG) y Goles Visitante (FTAG)
            ultimos = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].tail(5).to_string(index=False)
            resumen_datos += f"\n--- LIGA: {liga} ---\n{ultimos}\n"
        except Exception as e:
            resumen_datos += f"\nNo se pudo leer {liga}. Error: {e}\n"
            
    prompt = f"""
    Actúa como un analista cuantitativo experto. Usando principios de Sabermetrics y la distribución de Poisson,
    analiza los siguientes últimos resultados de las ligas europeas:
    
    {resumen_datos}
    
    Evalúa el rendimiento de goles (FTHG = Goles Local, FTAG = Goles Visitante). 
    1. Calcula qué equipos muestran la mejor proyección ofensiva actual.
    2. Sugiere 2 pronósticos de valor (CLV) para los próximos encuentros de estas ligas.
    """
    
    print("Iniciando motor de predicción europeo...")
    respuesta = model.generate_content(prompt)
    print("\n" + "="*40)
    print("🏆 PREDICCIONES EUROPEAS GENERADAS 🏆")
    print("="*40)
    print(respuesta.text)

if __name__ == "__main__":
    ejecutar_analisis()
