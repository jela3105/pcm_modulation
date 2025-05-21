import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def ruta_imagen(nombre_archivo):
    return os.path.join(BASE_DIR, "images", nombre_archivo)

def ruta_audio(nombre_archivo):
    return os.path.join(BASE_DIR, "audio", nombre_archivo)

def ruta_assets(nombre_archivo):
    return os.path.join(BASE_DIR, "assets", nombre_archivo)

def ruta_guardado(nombre_archivo, carpeta):
    return os.path.join(BASE_DIR, carpeta, nombre_archivo)