import os
import pandas as pd
from google import genai

# Conexión usando el nuevo SDK de Google
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    # Lista exacta de los archivos CSV europeos
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
    Actúa como un analista cuantitativo experto. Usando principios de Sabermetrics, la distribución de Poisson, aproximaciones de xG (goles esperados) y el Criterio de Kelly, analiza los siguientes resultados recientes:
    
    {resumen_datos}
    
    Evalúa el rendimiento (FTHG = Goles Local, FTAG = Goles Visitante). 
    1. Calcula qué equipos muestran la mejor proyección ofensiva actual.
    2. Sugiere 2 pronósticos de valor (CLV) para los próximos encuentros de estas ligas.
    3. Recomienda cómo estructurar el tamaño de la inversión usando el Criterio de Kelly.
    """
    
    print("Iniciando motor de predicción europeo con el nuevo SDK...")
    
    # Llamada a la API de Gemini
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    # 1. Mostrar en la consola de GitHub Actions
    print("\n" + "="*40)
    print("🏆 PREDICCIONES EUROPEAS GENERADAS 🏆")
    print("="*40)
    print(response.text)

    # 2. Guardar el resultado físicamente en el repositorio
    print("\nGuardando el reporte en REPORTE_EUROPEO.md...")
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write("# 🏆 Análisis Cuantitativo Europeo\n\n")
        archivo.write(response.text)

if __name__ == "__main__":
    ejecutar_analisis()
