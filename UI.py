import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de tres filas")
        self.create_widgets()

    def create_widgets(self):
        # Fila 1: Gráfica
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill=tk.BOTH, expand=True)

        self.plot_graph_button = tk.Button(self.frame1, text="Graficar", command=self.plot_graph)
        self.plot_graph_button.pack(pady=10)

        # Fila 2: Dropdown de 8 números y dos botones
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill=tk.BOTH)

        options = [str(i) for i in range(1, 9)]
        self.selected_option1 = tk.StringVar()
        self.dropdown1 = ttk.Combobox(self.frame2, textvariable=self.selected_option1, values=options)
        self.dropdown1.pack(side=tk.LEFT, padx=10)

        self.button1 = tk.Button(self.frame2, text="Botón 1")
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2 = tk.Button(self.frame2, text="Botón 2")
        self.button2.pack(side=tk.LEFT, padx=10)

        # Fila 3: Dropdown de 8 números y dos imágenes
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill=tk.BOTH)

        self.selected_option2 = tk.StringVar()
        self.dropdown2 = ttk.Combobox(self.frame3, textvariable=self.selected_option2, values=options)
        self.dropdown2.pack(side=tk.LEFT, padx=10)

        # Cargamos las imágenes
        self.image1 = Image.open("imagen2.jpg")  # Reemplaza "image1.jpg" por la ruta de tu imagen
        self.image1 = self.image1.resize((100, 100), Image.BILINEAR)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label_image1 = tk.Label(self.frame3, image=self.photo1)
        self.label_image1.image = self.photo1
        self.label_image1.pack(side=tk.LEFT, padx=10)

        self.image2 = Image.open("imagen2.jpg")  # Reemplaza "image2.jpg" por la ruta de tu imagen
        self.image2 = self.image2.resize((100, 100), Image.BILINEAR)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label_image2 = tk.Label(self.frame3, image=self.photo2)
        self.label_image2.image = self.photo2
        self.label_image2.pack(side=tk.LEFT, padx=10)

    def plot_graph(self):
        # Limpiar la gráfica anterior si existe
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()

        # Generar nuevos datos para la gráfica
        x = np.linspace(0, 10, 100)
        y = np.cos(x)

        # Graficar los nuevos datos
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Gráfico')
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