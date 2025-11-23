import pyautogui
import time

print(" Mueve el mouse a la esquina SUPERIOR IZQUIERDA del área...")
time.sleep(5)
x1, y1 = pyautogui.position()

print(" Ahora mueve el mouse a la esquina INFERIOR DERECHA del área...")
time.sleep(5)
x2, y2 = pyautogui.position()

ancho = x2 - x1
alto = y2 - y1

# Imprime directamente en formato listo para copiar y pegar
print(f"x, y, ancho, alto = {x1}, {y1}, {ancho}, {alto}")
