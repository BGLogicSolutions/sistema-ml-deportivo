import os
import pandas as pd
from google import genai

# Conexión usando el nuevo SDK de Google
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
    Actúa como un analista cuantitativo experto. Usando principios de Sabermetrics y la distribución de Poisson,
    analiza los siguientes últimos resultados de las ligas europeas:
    
    {resumen_datos}
    
    Evalúa el rendimiento de goles (FTHG = Goles Local, FTAG = Goles Visitante). 
    1. Calcula qué equipos muestran la mejor proyección ofensiva actual.
    2. Sugiere 2 pronósticos de valor (CLV) para los próximos encuentros de estas ligas.
    """
    
    print("Iniciando motor de predicción europeo con el nuevo SDK...")
    
    # Llamada a la API usando la nueva estructura
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    print("\n" + "="*40)
    print("🏆 PREDICCIONES EUROPEAS GENERADAS 🏆")
    print("="*40)
    print(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
