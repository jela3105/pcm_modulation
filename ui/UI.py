import tkinter as tk
import cv2
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from processing.cuantizacion import cuantizacion
from graphs.grafica_BPSK import MBPSK
import numpy as np
import soundfile as sf
import pygame
import sounddevice as sd
from PIL import Image, ImageTk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto de Cuantización PCM")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f9f9f9")

        self.photo2 = None
        self.crear_widgets()

    def reproducir_audio(self, ruta):
        pygame.mixer.init()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def seleccion_dropdown1(self, event):
        opcion = self.dropdown1.get()
        audio, fs = sf.read("audio/audio_mono.mp3")
        audio_cuantizado = cuantizacion(int(opcion), audio, False)
        audio_cuantizado.imprimir_valores()
        resultado_audio = audio_cuantizado.recuantizar_data()
        sf.write("audio/audio_recuantizado.mp3", np.ravel(resultado_audio), fs)
        self.desplegar_grafica(resultado_audio)

    def seleccion_dropdown2(self, event):
        opcion = self.dropdown2.get()
        imagen = cv2.imread("images/imagen_gris.jpg")
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen_cuantizada = cuantizacion(int(opcion), imagen, True)
        imagen_cuantizada.imprimir_valores()
        ruta_cuantizada = "images/imagen_cuantizada.jpg"
        cv2.imwrite(ruta_cuantizada, imagen_cuantizada.recuantizar_data())
        nueva_img = ImageTk.PhotoImage(Image.open(ruta_cuantizada).resize((300, 200), Image.ADAPTIVE))
        self.label_image2.configure(image=nueva_img)
        self.label_image2.image = nueva_img

    def reproducir_audio_original(self):
        self.reproducir_audio("audio/audio_mono.mp3")

    def reproducir_audio_recuantizado(self):
        self.reproducir_audio("audio/audio_recuantizado.mp3")

    def crear_widgets(self):
        estilo_boton = {"font": ("Arial", 10), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5, "bd": 0}

        # Título
        tk.Label(self.root, text="Procesamiento PCM", font=("Arial", 16, "bold"), bg="#f9f9f9").pack(pady=10)

        # === SECCIÓN AUDIO ===
        audio_frame = tk.LabelFrame(self.root, text="Sección de Audio", padx=10, pady=10, bg="#f9f9f9", font=("Arial", 12, "bold"))
        audio_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        self.selected_option1 = tk.StringVar(value='8')
        options = [str(i) for i in range(1, 9)]

        self.dropdown1 = ttk.Combobox(audio_frame, textvariable=self.selected_option1, values=options, width=5)
        self.dropdown1.bind("<<ComboboxSelected>>", self.seleccion_dropdown1)
        self.dropdown1.grid(row=0, column=0, padx=10)

        tk.Button(audio_frame, text="Reproducir audio original", command=self.reproducir_audio_original, **estilo_boton).grid(row=0, column=1, padx=10)
        tk.Button(audio_frame, text="Reproducir audio recuantizado", command=self.reproducir_audio_recuantizado, **estilo_boton).grid(row=0, column=2, padx=10)

        self.canvas = None  # Inicializar canvas de gráfica

        # === SECCIÓN IMAGEN ===
        imagen_frame = tk.LabelFrame(self.root, text="Sección de Imagen", padx=10, pady=10, bg="#f9f9f9", font=("Arial", 12, "bold"))
        imagen_frame.pack(fill=tk.BOTH, padx=20, pady=10)

        self.selected_option2 = tk.StringVar(value='8')
        self.dropdown2 = ttk.Combobox(imagen_frame, textvariable=self.selected_option2, values=options, width=5)
        self.dropdown2.bind("<<ComboboxSelected>>", self.seleccion_dropdown2)
        self.dropdown2.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(imagen_frame, text="Imagen original", bg="#f9f9f9", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
        self.image1 = Image.open("images/imagen_gris.jpg").resize((300, 200), Image.ADAPTIVE)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = tk.Label(imagen_frame, image=self.photo1)
        self.label_image1.image = self.photo1
        self.label_image1.grid(row=1, column=1, padx=10)

        tk.Label(imagen_frame, text="Imagen recuantizada", bg="#f9f9f9", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)
        self.image2 = Image.open("images/imagen_gris.jpg").resize((300, 200), Image.ADAPTIVE)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label_image2 = tk.Label(imagen_frame, image=self.photo2)
        self.label_image2.image = self.photo2
        self.label_image2.grid(row=1, column=2, padx=10)

        self.frame_grabacion = tk.LabelFrame(self.root, text="Grabación de Audio", padx=10, pady=10, bg="#f2f2f2", font=("Arial", 11, "bold"), fg="black")
        self.frame_grabacion.pack(fill=tk.BOTH, padx=20, pady=10)

        self.boton_grabar = tk.Button(self.frame_grabacion, text="Grabar audio estéreo", command=self.grabar_audio_estereo, **estilo_boton)
        self.boton_grabar.pack(side=tk.LEFT, padx=10)

        self.boton_convertir = tk.Button(self.frame_grabacion, text="Convertir a mono", command=self.convertir_audio_a_mono, **estilo_boton)
        self.boton_convertir.pack(side=tk.LEFT, padx=10)

        self.boton_reproducir_estereo = tk.Button(
            self.frame_grabacion,
            text="Reproducir grabación estéreo",
            command=lambda: self.reproducir_audio("audio/grabacion_dos_canales.wav"),
            **estilo_boton
        )
        self.boton_reproducir_estereo.pack(side=tk.LEFT, padx=10)

        self.boton_reproducir_mono = tk.Button(
            self.frame_grabacion,
            text="Reproducir grabación mono",
            command=lambda: self.reproducir_audio("audio/grabacion_mono.wav"),
            **estilo_boton
        )
        self.boton_reproducir_mono.pack(side=tk.LEFT, padx=10)


    def desplegar_grafica(self, audio=None):
        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.get_tk_widget().destroy()

        if audio is None:
            return

        plt.figure(figsize=(14, 4))
        plt.plot(audio)
        plt.xlabel('Tiempo')
        plt.ylabel('Amplitud')
        plt.title('Señal de audio recuantizado')
        plt.grid(True)

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)

    def seleccionar_microfono_2_canales_real(self, fs=8000, prueba_segundos=1):
        for i, device in enumerate(sd.query_devices()):
            name = device['name'].lower()
            if device['max_input_channels'] >= 2:
                # Evitar dispositivos virtuales
                if any(virtual in name for virtual in ["virtual", "assign", "asignador", "wave", "oculus", "mix", "speaker"]):
                    nombre = device["name"]
                    print(f"Dispositivo {i} ignorado por nombre sospechoso: {nombre}")

                    continue
                try:
                    print(f"Probando micrófono {i}: {device['name']}")
                    sd.default.device = (i, None)
                    prueba = sd.rec(int(prueba_segundos * fs), samplerate=fs, channels=2, dtype='float64')
                    sd.wait()

                    if np.any(prueba):
                        print(f"Micrófono válido encontrado: {device['name']} (índice {i})")
                        return i
                    else:
                        print("Micrófono sin señal de audio. Se descarta.")
                except Exception as e:
                    print(f"Fallo con índice {i}: {e}")
        raise RuntimeError("No se encontró un micrófono físico de 2 canales que funcione.")

    
    
    def grabar_audio_estereo(self, duracion=10, fs=8000):
        print("Buscando micrófono válido de 2 canales y funcional...")
        index = self.seleccionar_microfono_2_canales_real(fs=fs)  # obtiene el índice válido
        sd.default.device = (index, None)  # lo asigna explícitamente
        print("Iniciando grabación de audio...")

        audio = sd.rec(int(duracion * fs), samplerate=fs, channels=2, dtype='float64')
        sd.wait()
        sf.write("audio/grabacion_dos_canales.wav", audio, fs)
        print("Grabación estéreo completada y guardada en 'grabacion_dos_canales.wav'")
    
    def convertir_audio_a_mono(self, nombre_entrada="audio/grabacion_dos_canales.wav", nombre_salida="audio/grabacion_mono.wav"):
        audio, fs = sf.read(nombre_entrada)
        if audio.ndim == 2:
            audio_mono = (audio[:, 0] + audio[:, 1]) / 2.0
        else:
            audio_mono = audio
        sf.write(nombre_salida, audio_mono, fs)
        print(f"Audio convertido a mono y guardado como '{nombre_salida}'")


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

