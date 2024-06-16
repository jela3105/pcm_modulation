import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

# Función para crear el gráfico del seno
def create_sin_plot(parent):
<<<<<<< HEAD
=======
    fig, ax = plt.subplots(figsize=(12, 3))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title('Seno', fontsize=8)
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.tick_params(axis='both', which='minor', labelsize=6)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT)

# Función para crear el gráfico del coseno
def create_cos_plot(parent):
>>>>>>> parent of 41f6eb4 (Plot senal binaria y mostar imagenes)
    fig, ax = plt.subplots(figsize=(12, 3))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title('Seno', fontsize=8)
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
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT)

    # Función para cargar una imagen
    def create_image_label(self, parent, image_path):
        img = Image.open(image_path)
        img =img.resize((200, 200), Image.ADAPTIVE)
        photo = ImageTk.PhotoImage(img)
        self.label = tk.Label(parent, image=self.photo)
        self.label.image = photo
        self.label.pack(side=tk.LEFT)

    def crear_widgets(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Interfaz de Tres Filas")

        # Primera fila: Dropdown y gráfico de seno
        self.frame_row1 = tk.Frame(self.root)
        self.frame_row1.pack(fill=tk.X, pady=5)

    dropdown1 = ttk.Combobox(frame_row1, values=["Imagen", "Audio"])
    dropdown1.pack(side=tk.LEFT, padx=10)
    
    create_sin_plot(frame_row1)

        # Segunda fila: Dropdown y gráfico de coseno
        self.frame_row2 = tk.Frame(self.root)
        self.frame_row2.pack(fill=tk.X, pady=5)

        self.dropdown2 = ttk.Combobox(self.frame_row2, values=[str(i) for i in range(1, 9)])
        self.dropdown2.pack(side=tk.LEFT, padx=10)
        
        self.create_cos_plot(self.frame_row2)

        # Tercera fila: Dos imágenes y dropdown
        self.frame_row3 = tk.Frame(self.root)
        self.frame_row3.pack(fill=tk.X, pady=10)

    create_image_label(frame_row3, "image.jpeg")  # Reemplaza con la ruta de tu imagen
    create_image_label(frame_row3, "image.jpeg")  # Reemplaza con la ruta de tu imagen

        self.dropdown3 = ttk.Combobox(self.frame_row3, values=["BPSK", "8PSK", "16QAM"])
        self.dropdown3.pack(side=tk.LEFT, padx=10)

def main():
    root = tk.Tk()
    gui = GUI2(root)
    root.mainloop()

if __name__ == "__main__":
    main()
