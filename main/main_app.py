import cv2
import tkinter as tk
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from ui.UI import GUI
import numpy as np

# Convertir imagen a escala de grises
def convertir_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    print("Imagen gris:", imagen_gris)
    return imagen_gris

# Binarizar imagen con umbral
def binarizar_imagen(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, imagen_binarizada = cv2.threshold(imagen_gris, 127, 1, cv2.THRESH_BINARY_INV)
    print("Imagen blanco negro:", imagen_binarizada)
    return imagen_binarizada

# Leer imagen y procesarla
def leer_datos():
    ruta_imagen = "images/image.jpeg"
    imagen = cv2.imread(ruta_imagen)

    if imagen is None:
        print("Imagen no encontrada:", ruta_imagen)
        return

    imagen_binarizada = binarizar_imagen(imagen)
    imagen_gris = convertir_a_grises(imagen)
    cv2.imwrite("images/imagen_gris.jpg", imagen_gris)

    # Crear figura matplotlib
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Imagen Original')
    axs[0].axis('off')

    axs[1].imshow(imagen_gris, cmap='gray')
    axs[1].set_title('Imagen Escala de Grises')
    axs[1].axis('off')

    axs[2].imshow(imagen_binarizada, cmap='binary')
    axs[2].set_title('Imagen Binarizada')
    axs[2].axis('off')

    # Crear ventana tkinter
    ventana = tk.Tk()
    ventana.title("Visualización de Imágenes y Acceso a PCM")

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Botón dentro de la misma ventana
    boton_pcm = tk.Button(ventana, text="Ir a Interfaz PCM", font=("Arial", 12), command=lambda: [ventana.withdraw(), desplegar_interfaz()])
    boton_pcm.pack(pady=10)

    ventana.mainloop()

# Mostrar interfaz gráfica
def desplegar_interfaz():
    root = tk.Toplevel()
    gui = GUI(root)
    root.mainloop()

def main():
    leer_datos()

if __name__ == "__main__":
    main()
    