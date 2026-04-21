name: Ejecutar Modelo Cuantitativo Europeo

on: [push]

# Le damos permiso al bot para guardar archivos
permissions:
  contents: write

jobs:
  analisis:
    runs-on: ubuntu-latest
    
    steps:
      - name: Descargar el código
        uses: actions/checkout@v4

      - name: Configurar entorno
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Instalar librerías
        run: |
          python -m pip install --upgrade pip
          pip install google-genai pandas scipy

      - name: Ejecutar motor de predicción
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python prediccion.py

      - name: Guardar reporte generado en el repositorio
        run: |
          git config --global user.name 'Sistema Cuantitativo'
          git config --global user.email 'bot@modelo.com'
          git add REPORTE_EUROPEO.md
          git commit -m "📊 Nuevo análisis de valor generado" || echo "Sin cambios"
          git push
