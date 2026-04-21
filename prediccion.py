import os
import time
from datetime import datetime, timedelta, timezone
import pandas as pd
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ejecutar_analisis():
    zona_horaria = timezone(timedelta(hours=-6))
    hoy = datetime.now(zona_horaria).date()
    fecha_str = hoy.strftime("%d/%m/%Y")
    print(f"Buscando partidos para hoy: {fecha_str}")
    
    # --- 1. LEER LA MEMORIA DE AYER ---
    try:
        with open("BITACORA.txt", "r", encoding="utf-8") as f:
            memoria_ayer = f.read()
    except FileNotFoundError:
        memoria_ayer = "No hay registro de predicciones anteriores para auditar."

    archivos_masivos = {
        "La Liga": "Laliga2326.csv",
        "Premier League": "Premier2326.csv",
        "Serie A": "SerieA2326.csv",
        "Bundesliga": "Bundesliga2326.csv"
    }
    
    contexto_para_ia = ""
    partidos_encontrados = False
    
    for liga, archivo in archivos_masivos.items():
        try:
            df = pd.read_csv(archivo, low_memory=False)
            df['Fecha_Limpia'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce').dt.date
            partidos_hoy = df[df['Fecha_Limpia'] == hoy]
            
            if not partidos_hoy.empty:
                partidos_encontrados = True
                contexto_para_ia += f"\n\n--- 🏆 {liga.upper()} (HOY) ---\n"
                
                for _, partido in partidos_hoy.iterrows():
                    local = partido['HomeTeam']
                    visitante = partido['AwayTeam']
                    
                    historial_local = df[(df['HomeTeam'] == local) | (df['AwayTeam'] == local)].tail(5)
                    historial_visitante = df[(df['HomeTeam'] == visitante) | (df['AwayTeam'] == visitante)].tail(5)
                    
                    contexto_para_ia += f"⚽ {local} vs {visitante}\n"
                    contexto_para_ia += f"Últimos 5 de {local}:\n{historial_local[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    contexto_para_ia += f"Últimos 5 de {visitante}:\n{historial_visitante[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False)}\n"
                    
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")

    if not partidos_encontrados:
        print("No hay partidos para hoy.")
        return

    # --- 2. EL PROMPT EVOLUTIVO (AUDITORÍA + PREDICCIÓN) ---
    prompt = f"""
    Actúa como un analista cuantitativo deportivo. Hoy es {fecha_str}.
    
    FASE 1: AUDITORÍA DE TUS ERRORES (SELF-REFLECTION)
    Este es el registro de tu último análisis:
    {memoria_ayer}
    
    Instrucción de Auditoría:
    - Usa tu herramienta de BÚSQUEDA EN GOOGLE para investigar el resultado real de esos partidos.
    - Si tu predicción fue errónea (ej. predijiste 2-1 y fue 4-3), realiza un diagnóstico crítico: ¿Subestimaste el xG visitante? ¿La distribución de Poisson falló por una expulsión o clima que no viste? ¿Tu cálculo del Criterio de Kelly fue demasiado agresivo?
    - Ajusta tu lógica matemática internamente basándote en este error.

    FASE 2: PROYECCIONES DE HOY (CALIBRADAS)
    Basado en tu nuevo aprendizaje y el historial cruzado, analiza los partidos de HOY:
    {contexto_para_ia}
    
    Instrucciones de Predicción:
    1. Busca noticias en vivo de estos equipos.
    2. Aplica Poisson y Sabermetrics con la calibración que obtuviste en la Fase 1.
    3. Entrega el pronóstico de valor (CLV).
    4. Sugiere la gestión de capital con Kelly.
    """
    
    print("Iniciando IA con Auditoría de errores y búsqueda en Internet...")
    
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
                time.sleep(20)
                if intento == max_reintentos - 1: return
            else:
                return
    
    # --- 3. GUARDAR EL REPORTE Y LA NUEVA BITÁCORA ---
    print("\nGuardando reporte y actualizando la memoria...")
    
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write(f"# 📊 Análisis Diario y Auditoría: {fecha_str}\n\n")
        archivo.write(response.text)

    # Extraemos solo un resumen de la predicción de hoy para que la lea mañana
    resumen_para_manana = f"Predicciones hechas el {fecha_str} para los partidos: {contexto_para_ia}"
    with open("BITACORA.txt", "w", encoding="utf-8") as bitacora:
        bitacora.write(resumen_para_manana + "\n(Busca en internet qué predijiste exactamente en tu respuesta y compáralo con el resultado real).")

if __name__ == "__main__":
    ejecutar_analisis()
