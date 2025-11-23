import pyautogui
import datetime
import os
import ollama

# 1. Crear carpeta "capturas" en el mismo lugar del script
carpeta = os.path.join(os.path.dirname(__file__), "../capturas")
os.makedirs(carpeta, exist_ok=True)

# 2. Definir coordenadas (x, y, ancho, alto)
# Si las dejas en None, se captura toda la pantalla
x, y, ancho, alto = 40, 412, 902, 511

# 3. Tomar captura según coordenadas
nombre_archivo = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
ruta_imagen = os.path.join(carpeta, nombre_archivo)

if None not in (x, y, ancho, alto):
    # Captura región definida
    captura = pyautogui.screenshot(region=(x, y, ancho, alto))
else:
    # Captura toda la pantalla
    captura = pyautogui.screenshot()

captura.save(ruta_imagen)
print(f"✅ Captura guardada en: {ruta_imagen}")

# 4. Prompt que quieres enviar al modelo
""""

"""
prompt = ("describe la imagen")

# 5. Enviar imagen + prompt al modelo multimodal (ejemplo: llava)
response = ollama.chat(
    model="llava",  # puedes cambiarlo por "qwen-vl" si lo tienes instalado
    messages=[
        {
            "role": "user",
            "content": prompt,
            "images": [ruta_imagen]
        }
    ]
)

print(" Respuesta del modelo:")
print(response["message"]["content"])
