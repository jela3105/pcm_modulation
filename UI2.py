import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from cuantizacion import cuantizacion
from grafica_BPSK import MBPSK
from grafica_8PSK import M8PSK
from grafica_16QAM import M16QAM
import cv2
import soundfile as sf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

class UI2:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Tres Filas")
        
        # Primera fila: Dropdown y gráfico codigo pcm (bits) 
        self.frame_row1 = tk.Frame(root)
        self.frame_row1.pack(fill=tk.X, pady=5)
        self.dropdown1 = ttk.Combobox(self.frame_row1, values=["Imagen", "Audio"])
        self.dropdown1.pack(side=tk.LEFT, padx=10)
        self.dropdown1.bind("<<ComboboxSelected>>", self.seleccion_tipo_archivo)
        self.dropdown1.current(0)
        #self.mostrar_graficas_modulacion()

        # Segunda fila: Dropdown y gráfico senal modulada
        self.frame_row2 = tk.Frame(root)
        self.frame_row2.pack(fill=tk.X, pady=5)
        self.dropdown2 = ttk.Combobox(self.frame_row2, values=[str(i) for i in range(1, 9)])
        self.dropdown2.pack(side=tk.LEFT, padx=10)
        self.dropdown2.bind("<<ComboboxSelected>>", self.seleccion_n)
        #self.create_cos_plot(self.frame_row2)

        # Tercera fila: Dos imágenes y dropdown
        self.frame_row3 = tk.Frame(root)
        self.frame_row3.pack(fill=tk.X, pady=10)
        self.imagen1_label = self.create_image_label(self.frame_row3, "imagen_gris.jpg")
        self.imagen2_label = self.create_image_label(self.frame_row3, "imagen_cuantizada.jpg")
        self.dropdown3 = ttk.Combobox(self.frame_row3, values=["BPSK", "8PSK", "16QAM"])
        self.dropdown3.pack(side=tk.LEFT, padx=10)
        self.dropdown3.current(0)
        self.dropdown3.bind("<<ComboboxSelected>>", self.mostrar_graficas_modulacion)

        self.button1 = tk.Button(self.frame_row3, text="Audio original")
        self.button2 = tk.Button(self.frame_row3, text="Audio recuantizado")
        self.button1.pack_forget()
        self.button2.pack_forget()
    
    # modifica los valores de las graficas
    def mostrar_graficas_modulacion(self, event):
        if self.dropdown3.get() == "BPSK":
            bits_usados = self.crear_senal_pcm(self.frame_row1, 7)
            MBPSK(bits_usados)

        elif self.dropdown3.get() == "8PSK":
            bits_usados = self.crear_senal_pcm(self.frame_row1, 21)
            M8PSK(bits_usados)

        elif self.dropdown3.get() == "16QAM":
            bits_usados = self.crear_senal_pcm(self.frame_row1, 28)
            M16QAM(bits_usados)
   
    def seleccion_n(self, event):
        numero_n_seleccionado = self.dropdown2.get()
        if self.dropdown1.get() == "Imagen":
            img_modificar = cv2.imread("imagen_gris.jpg")
            img_modificar = cv2.cvtColor(img_modificar, cv2.COLOR_BGR2GRAY)
            imagen_cuantizada = cuantizacion(int(numero_n_seleccionado), img_modificar, True)
            imagen_cuantizada.imprimir_valores()
            cv2.imwrite("imagen_cuantizada.jpg", imagen_cuantizada.recuantizar_data())
            nueva_img = ImageTk.PhotoImage(Image.open("imagen_cuantizada.jpg").resize((300, 200), Image.ADAPTIVE))
            self.imagen2_label.configure(image= nueva_img)
            self.imagen2_label.image = nueva_img
        else:
            audio, fs = sf.read("audio_mono.mp3")
            audio_cuantizado = cuantizacion(int(numero_n_seleccionado), audio, False)
            audio_cuantizado.imprimir_valores()
            resultado_audio = audio_cuantizado.recuantizar_data()
            sf.write("audio_recuantizado.mp3", np.ravel(resultado_audio), fs)
        self.mostrar_graficas_modulacion(None)

    # Función para crear el gráfico de bits
    def crear_senal_pcm(self, parent, bits_a_usar):
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(12, 3))

        #decidimos si mostrar el pcm de la imagen o del audio 
        if self.dropdown1.get() == "Imagen":
            nombre_archivo = "imagen_codigo_pcm.txt"
        else:
            nombre_archivo = "audio_codigo_pcm.txt"

        with open(nombre_archivo, 'r',encoding="UTF-8") as file:
            # lee el numero de bits a usar
            primeros_chars = file.read(bits_a_usar) #para que no se agarre todo el archivo, pero si suficientes para los baudios necesarios

        primeros_bits = [int(char) for char in primeros_chars]#convierte cada elemento a entero
        ax.step(np.arange(len(primeros_bits)), primeros_bits, where='mid')
        ax.set_title('Senal modulada (codigo binario)', fontsize=8)
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT)
        return primeros_bits

    # Función para cargar una imagen
    def create_image_label(self, parent, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 200), Image.ADAPTIVE)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(parent, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT)
        return label
    
    def seleccion_tipo_archivo(self, event):
        if self.dropdown1.get() == "Audio":
            self.imagen1_label.pack_forget()
            self.imagen2_label.pack_forget()
            self.button1.pack(side=tk.LEFT, padx=5)
            self.button2.pack(side=tk.LEFT, padx=5)
        else:
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.imagen1_label.pack(side=tk.LEFT)
            self.imagen2_label.pack(side=tk.LEFT)
        self.mostrar_graficas_modulacion(event)

def main():
    root = tk.Tk()
    app = UI2(root)
    root.mainloop()

if __name__ == "__main__":
    main()