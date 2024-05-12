import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cuantizacion import cuantizacion
import numpy as np
import soundfile as sf
from PIL import Image, ImageTk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Opciones PCM")
        self.crear_widgets()

    def seleccion_dropdown1(self, event):
        opcion_seleccionada = self.dropdown1.get()
        print("N seleccionado de dropdown 1:", opcion_seleccionada)
        audio, fs = sf.read("audio_mono.mp3")
        audio_cuantizado = cuantizacion(int(opcion_seleccionada), audio, False)
        audio_cuantizado.imprimir_valores()
        sf.write("audio_recuantizado.mp3", audio_cuantizado.recuantizar_data(), fs)

    def seleccion_dropdown2(self, event):
        opcion_seleccionada = self.dropdown2.get()
        print("N seleccionado de dropdown 2:", opcion_seleccionada)
        imagen_cuantizada = cuantizacion(int(opcion_seleccionada), Image.open("imagen_gris.jpg"), True)
        imagen_cuantizada.imprimir_valores()

    def reproducir_audio(self):
        print("reproducir audio original")

    def reproducir_audio_recuantizado(self):
        print("reproducir audio recuantizado")

    def crear_widgets(self):
        # Fila 1: Gráfica
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill=tk.BOTH, expand=True)

        self.plot_graph_button = tk.Button(self.frame1, text="Graficar", command=self.desplegar_grafica)
        self.plot_graph_button.pack(pady=10)

        # Fila 2: Dropdown de 8 números y dos botones
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill=tk.BOTH)

        options = [str(i) for i in range(1, 9)]
        self.selected_option1 = tk.StringVar()
        self.selected_option1.set('8')
        self.dropdown1 = ttk.Combobox(self.frame2, textvariable=self.selected_option1, values=options)
        self.dropdown1.bind("<<ComboboxSelected>>", self.seleccion_dropdown1)
        self.dropdown1.pack(side=tk.LEFT, padx=10)

        self.button1 = tk.Button(self.frame2, text="Reproducir audio original", command=self.reproducir_audio)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2 = tk.Button(self.frame2, text="Reproducir audio recuantizado", command=self.reproducir_audio_recuantizado)
        self.button2.pack(side=tk.LEFT, padx=10)

        # Fila 3: Dropdown de 8 números y dos imágenes
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill=tk.BOTH)

        self.selected_option2 = tk.StringVar()
        self.selected_option2.set('8')
        self.dropdown2 = ttk.Combobox(self.frame3, textvariable=self.selected_option2, values=options)
        self.dropdown2.bind("<<ComboboxSelected>>", self.seleccion_dropdown2)

        self.dropdown2.pack(side=tk.LEFT, padx=10)

        # Cargamos las imágenes
        self.title_label1 = tk.Label(self.frame3, text="Imagen original")
        self.title_label1.pack(side=tk.LEFT, padx=9)
        self.image1 = Image.open("imagen_gris.jpg")  # Reemplaza "image1.jpg" por la ruta de tu imagen
        self.image1 = self.image1.resize((300, 200), Image.ADAPTIVE)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = tk.Label(self.frame3, image=self.photo1)
        self.label_image1.image = self.photo1
        self.label_image1.pack(side=tk.LEFT, padx=10)

        self.title_label2 = tk.Label(self.frame3, text="Imagen recuantizada")
        self.title_label2.pack(side=tk.TOP, padx=10)
        self.image2 = Image.open("imagen_gris.jpg")  # Reemplaza "image2.jpg" por la ruta de tu imagen
        self.image2 = self.image2.resize((300, 200), Image.ADAPTIVE)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label_image2 = tk.Label(self.frame3, image=self.photo2)
        self.label_image2.image = self.photo2
        self.label_image2.pack(side=tk.LEFT, padx=10)

    def desplegar_grafica(self):
        # Limpiar la gráfica anterior si existe
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()

        print("actualizar grafica")
        # Generar nuevos datos para la gráfica
        x = np.linspace(0, 10, 100)
        y = np.cos(x)

        # Graficar los nuevos datos
        plt.figure(figsize=(8,2))
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Audio recuantizado (mono)')
        plt.grid(True)

        # Crear la gráfica dentro del widget de Tkinter
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()