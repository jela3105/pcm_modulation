import tkinter as tk
from ui.UI2 import UI2

def main():
    root = tk.Tk()
    root.title("Visualizador de Modulación Digital")
    app = UI2(root)
    root.mainloop()

if __name__ == "__main__":
    main()
