import cv2
import tkinter as tk
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
from UI import GUI

# Función para convertir una imagen a escala de grises
def convertir_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    print(f"Imagen gris: {imagen_gris}")
    return imagen_gris

# Función para binarizar una imagen
def binarizar_imagen(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para binarizar la imagen
    _, imagen_binarizada = cv2.threshold(imagen_gris, 127, 1, cv2.THRESH_BINARY_INV)
    
    print(f"Imagen blanco negro: {imagen_binarizada}")
    return imagen_binarizada

def grabar_audio(duracion, fs):
    print("Grabando...")

    # Grabar audio en dos canales
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Esperar hasta que la grabación se complete
    print("Grabación completada.")
    print(f"Grabacion dos canales: {audio}")
    sf.write("grabacion_dos_canales.wav", audio, fs)
    print(f"Grabación guardada.")

def convertir_mono(nombre_archivo_entrada, nombre_archivo_salida):
    # Cargar el archivo de audio de dos canales
    audio, fs = sf.read(nombre_archivo_entrada)

    # Promediar los datos de los dos canales para obtener un solo canal
    audio_mono = (audio[:, 0] + audio[:, 1]) / 2.0

    print(f"Conversion un canal: {audio_mono}")
    # Guardar la grabación en un archivo WAV mono
    sf.write(nombre_archivo_salida, audio_mono, fs)
    print(f"Archivo convertido y guardado como '{nombre_archivo_salida}'.")

def leer_datos():
    # Ruta de la imagen a leer
    ruta_imagen = "imagen2.jpg"

    # Leer la imagen
    imagen = cv2.imread(ruta_imagen)
    print(imagen)
    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("Imagen no encontrada")
        return

    # Binarizar la imagen
    imagen_binarizada = binarizar_imagen(imagen)

    # Convertir la imagen a escala de grises
    imagen_gris = convertir_a_grises(imagen)
            
    plt.figure(figsize=(12, 4))
        
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')
        
    plt.subplot(132)
    plt.imshow(imagen_gris, cmap='gray')
    plt.title('Imagen Escala de Grises')
    plt.axis('off')
        
    plt.subplot(133)
    plt.imshow(imagen_binarizada, cmap='binary')
    plt.title('Imagen Binarizada')
    plt.axis('off')
      
    plt.show()
         
    # Grabacion de sonido   
    print("Inicio de grabacion")
    duracion = 10 # Durancion de grabacion en segundos
    fs = 8000 #frecuencia de muestreo
    grabar_audio(duracion, fs)
    convertir_mono("grabacion_dos_canales.wav", "grabacion_mono.wav")

    # Leer audio
    print("Leyendo y convirtiendo audio estereo a mono")
    convertir_mono("audio_estereo.mp3", "audio_mono.mp3")   

def desplegar_interfaz():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

def main():
    leer_datos()
    desplegar_interfaz()

if __name__ == "__main__":
    main()
