import os
import time
import requests
from datetime import datetime, timedelta, timezone
import pandas as pd
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def enviar_telegram(mensaje):
    """Función para mandar el reporte directo a tu celular"""
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            # Mandamos los primeros 4000 caracteres (límite de Telegram)
            requests.post(url, data={'chat_id': chat_id, 'text': mensaje[:4000]})
            print("🚀 Reporte enviado por Telegram al patrón.")
        except Exception as e:
            print(f"⚠️ Falló el envío a Telegram: {e}")

def ejecutar_analisis():
    zona_horaria = timezone(timedelta(hours=-6))
    hoy = datetime.now(zona_horaria).date()
    fecha_str = hoy.strftime("%d/%m/%Y")
    print(f"Iniciando Agente Autónomo. Fecha: {fecha_str}")
    
    archivos_masivos = {
        "La Liga": "Laliga2326.csv",
        "Premier League": "Premier2326.csv",
        "Serie A": "SerieA2326.csv",
        "Bundesliga": "Bundesliga2326.csv"
    }
    
    # 1. Recopilar todos los equipos disponibles y leer los CSV
    dataframes = {}
    equipos_conocidos = set()
    
    for liga, archivo in archivos_masivos.items():
        try:
            df = pd.read_csv(archivo, low_memory=False)
            dataframes[liga] = df
            equipos_conocidos.update(df['HomeTeam'].dropna().unique())
            equipos_conocidos.update(df['AwayTeam'].dropna().unique())
        except Exception as e:
            print(f"Aviso: No se pudo cargar {archivo} - {e}")

    if not equipos_conocidos:
        print("Error: No se pudo leer ningún equipo de las bases de datos.")
        return

    lista_equipos_str = ", ".join(sorted(list(equipos_conocidos)))

    # ==========================================
    # FASE 1: EXPLORACIÓN (BLINDADA CON BACKOFF)
    # ==========================================
    prompt_explorador = f"""
    Hoy es {fecha_str}. Eres un buscador de calendarios deportivos.
    Usa tu herramienta de BÚSQUEDA EN GOOGLE para investigar qué partidos de las ligas principales (España, Inglaterra, Italia, Alemania) se juegan el día de HOY.
    
    IMPORTANTE: De los equipos que juegan hoy, necesito que cruces sus nombres con esta lista exacta de equipos de mi base de datos:
    {lista_equipos_str}
    
    Devuelve ÚNICAMENTE los nombres EXACTOS de mi lista que juegan hoy, separados por comas. 
    Ejemplo de respuesta esperada: Real Madrid, Alaves, Ath Bilbao, Osasuna
    Si no hay partidos hoy, responde: NINGUNO
    """
    
    print("\nFase 1: Buscando partidos de hoy en Internet...")
    equipos_hoy = []
    
    for intento in range(3):
        try:
            respuesta_explorador = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_explorador,
                config=types.GenerateContentConfig(tools=[{"google_search": {}}])
            )
            if "NINGUNO" in respuesta_explorador.text.upper():
                print("La IA confirmó que no hay encuentros de las grandes ligas hoy.")
                return
                
            # Limpiamos y cruzamos con nuestra base de datos real
            equipos_hoy = [e.strip() for e in respuesta_explorador.text.split(',') if e.strip() in equipos_conocidos]
            break
        except Exception as e:
            print(f"⚠️ Intento {intento + 1} fallido en Fase 1: {e}")
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print("Servidores saturados, tomando un respiro de 20 segundos...")
                time.sleep(20)
                if intento == 2: return
            else: return

    if not equipos_hoy:
        print("No se encontraron coincidencias exactas de equipos para hoy.")
        return

    print(f"✅ Partidos encontrados para los equipos: {equipos_hoy}")

    # ==========================================
    # FASE 2: EXTRACCIÓN HISTÓRICA
    # ==========================================
    contexto_para_ia = ""
    for equipo in equipos_hoy:
        for liga, df in dataframes.items():
            historial = df[(df['HomeTeam'] == equipo) | (df['AwayTeam'] == equipo)].tail(5)
            if not historial.empty:
                contexto_para_ia += f"\n⚽ Últimos 5 de {equipo} ({liga}):\n"
                contexto_para_ia += historial[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].to_string(index=False) + "\n"
                break # Pasamos al siguiente equipo

    # Leer memoria de errores
    try:
        with open("BITACORA.txt", "r", encoding="utf-8") as f:
            memoria_ayer = f.read()
    except FileNotFoundError:
        memoria_ayer = "Sin registro previo."

    # ==========================================
    # FASE 3: ANÁLISIS CUANTITATIVO Y PREDICCIÓN (BLINDADA)
    # ==========================================
    prompt_analista = f"""
    Actúa como un analista cuantitativo deportivo. Hoy es {fecha_str}.
    
    1. MEMORIA Y AUDITORÍA: Revisa esta bitácora pasada, busca en internet cómo terminaron esos juegos y ajusta tus cálculos si te equivocaste:
    {memoria_ayer}
    
    2. ANÁLISIS DE HOY: Aquí tienes el historial reciente de los equipos que juegan HOY extraído directamente de nuestra base de datos:
    {contexto_para_ia}
    
    INSTRUCCIONES FINALES:
    - Busca en Google noticias en vivo de estos equipos (alineaciones, lesiones de hoy).
    - Aplica la distribución de Poisson y Sabermetrics sobre el historial proporcionado (xG).
    - Sugiere el pronóstico de mayor valor (CLV).
    - Recomienda el tamaño de inversión usando el Criterio de Kelly.
    """
    
    print("\nFase 2: Ejecutando cálculos de Poisson y Kelly con datos extraídos...")
    response = None
    
    for intento in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_analista,
                config=types.GenerateContentConfig(tools=[{"google_search": {}}])
            )
            break
        except Exception as e:
            print(f"⚠️ Intento {intento + 1} fallido en Fase 3: {e}")
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                time.sleep(20)
                if intento == 2: return
            else: return
    
    if not response:
        print("❌ No se pudo generar el análisis de valor.")
        return
        
    print("\nGuardando reporte y notificando...")
    
    # 1. Guardar Markdown
    with open("REPORTE_EUROPEO.md", "w", encoding="utf-8") as archivo:
        archivo.write(f"# 📊 Análisis Diario Evolutivo: {fecha_str}\n\n")
        archivo.write(response.text)

    # 2. Actualizar Bitácora
    with open("BITACORA.txt", "w", encoding="utf-8") as bitacora:
        bitacora.write(f"Partidos analizados el {fecha_str}:\n{contexto_para_ia}\nEvalúa tu margen de error.")

    # 3. Notificar por Telegram
    mensaje_telegram = f"🔥 REPORTE CUANTITATIVO - {fecha_str} 🔥\n\n{response.text}"
    enviar_telegram(mensaje_telegram)

if __name__ == "__main__":
    ejecutar_analisis()
