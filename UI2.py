import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

# Función para crear el gráfico del seno
def create_sin_plot(parent):
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
def create_image_label(parent, image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200), Image.ADAPTIVE)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(parent, image=photo)
    label.image = photo
    label.pack(side=tk.LEFT)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Interfaz de Tres Filas")

    # Primera fila: Dropdown y gráfico de seno
    frame_row1 = tk.Frame(root)
    frame_row1.pack(fill=tk.X, pady=5)

    dropdown1 = ttk.Combobox(frame_row1, values=["Imagen", "Audio"])
    dropdown1.pack(side=tk.LEFT, padx=10)
    
    create_sin_plot(frame_row1)

    # Segunda fila: Dropdown y gráfico de coseno
    frame_row2 = tk.Frame(root)
    frame_row2.pack(fill=tk.X, pady=5)

    dropdown2 = ttk.Combobox(frame_row2, values=[str(i) for i in range(1, 9)])
    dropdown2.pack(side=tk.LEFT, padx=10)
    
    create_cos_plot(frame_row2)

    # Tercera fila: Dos imágenes y dropdown
    frame_row3 = tk.Frame(root)
    frame_row3.pack(fill=tk.X, pady=10)

    create_image_label(frame_row3, "image.jpeg")  # Reemplaza con la ruta de tu imagen
    create_image_label(frame_row3, "image.jpeg")  # Reemplaza con la ruta de tu imagen

    dropdown3 = ttk.Combobox(frame_row3, values=["BPSK", "8PSK", "16QAM"])
    dropdown3.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
