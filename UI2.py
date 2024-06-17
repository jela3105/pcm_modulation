import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

class UI2:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Tres Filas")
        
        # Primera fila: Dropdown y gráfico de seno
        self.frame_row1 = tk.Frame(root)
        self.frame_row1.pack(fill=tk.X, pady=5)
        self.dropdown1 = ttk.Combobox(self.frame_row1, values=["Imagen", "Audio"])
        self.dropdown1.pack(side=tk.LEFT, padx=10)
        self.crear_senal_modulada(self.frame_row1)

        # Segunda fila: Dropdown y gráfico de coseno
        self.frame_row2 = tk.Frame(root)
        self.frame_row2.pack(fill=tk.X, pady=5)
        self.dropdown2 = ttk.Combobox(self.frame_row2, values=[str(i) for i in range(1, 9)])
        self.dropdown2.pack(side=tk.LEFT, padx=10)
        self.create_cos_plot(self.frame_row2)

        # Tercera fila: Dos imágenes y dropdown
        self.frame_row3 = tk.Frame(root)
        self.frame_row3.pack(fill=tk.X, pady=10)
        self.create_image_label(self.frame_row3, "imagen_gris.jpg")
        self.create_image_label(self.frame_row3, "imagen_cuantizada.jpg")
        self.dropdown3 = ttk.Combobox(self.frame_row3, values=["BPSK", "8PSK", "16QAM"])
        self.dropdown3.pack(side=tk.LEFT, padx=10)

    # Función para crear el gráfico del seno
    def crear_senal_modulada(self, parent):
        fig, ax = plt.subplots(figsize=(12, 3))
        with open('audio_codigo_pcm.txt', 'r') as file:
            # Read the first 10 characters
            primeros_10_chars = file.read(10)
            primeros_bits = [int(char) for char in primeros_10_chars if char.isdigit()]
        ax.plot(primeros_bits)
        ax.set_title('Senal modulada (codigo binario)', fontsize=8)
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT)

    # Función para crear el gráfico del coseno
    def create_cos_plot(self, parent):
        fig, ax = plt.subplots(figsize=(12, 3))
        x = np.linspace(0, 10, 100)
        y = np.cos(x)
        ax.plot(x, y)
        ax.set_title('Coseno', fontsize=8)
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT)

    # Función para cargar una imagen
    def create_image_label(self, parent, image_path):
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.ADAPTIVE)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(parent, image=photo)
        label.image = photo
        label.pack(side=tk.LEFT)

def main():
    root = tk.Tk()
    app = UI2(root)
    root.mainloop()

if __name__ == "__main__":
    main()