import os
import google.generativeai as genai

# Conexión segura con tu llave
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest')


def ejecutar_analisis():
    # Aquí es donde combinas tus datos con la IA
    prompt = """
    Actúa como un analista cuantitativo experto.
    Basado en los principios de Sabermetrics y la distribución de Poisson,
    analiza el siguiente escenario para la Liga MX y calcula las probabilidades
    de victoria local, empate y visitante, sugiriendo si hay valor (CLV).
    
    Escenario: [AQUÍ LUEGO CONECTAREMOS TU ARCHIVO CSV DE DATOS]
    Equipo Local: América (xG promedio: 1.8)
    Equipo Visitante: Monterrey (xG promedio: 1.5)
    """
    
    respuesta = model.generate_content(prompt)
    print("--- RESULTADO DEL MODELO ---")
    print(respuesta.text)

if __name__ == "__main__":
    ejecutar_analisis()
