# PCM Modulation Interface

Este proyecto implementa una interfaz gráfica interactiva para el procesamiento de señales PCM (Modulación por Código de Pulsos), permitiendo trabajar con imágenes y audio para:

- Cuantización de señales.
- Visualización del código binario.
- Modulación con técnicas digitales como **BPSK**, **8PSK** y **16QAM**.
- Reproducción y grabación de audio.

## Capturas de pantalla

### Interfaz principal de procesamiento PCM
![PCM Processing Interface](assets/PCM%20Processing%20Interface.png)

### Interfaz de modulación digital
![PCM Modulation Interface](assets/PCM%20Modulation%20Interface.png)

### Gráfica de código binario generado
![Binarie Graphic](assets/Binarie%20Graphic.png)

### Gráfica de señal modulada
![graphic Modulation technique](assets/graphic%20Modulation%20technique.png)

### Gráfica de la señal completa
![Graphics Signal](assets/Graphics%20Signal.png)

Nota: Las imágenes deben estar en la carpeta `images/` y sin espacios

## Tecnologías usadas

- **Python 3.11**
- **Tkinter** – para interfaces gráficas.
- **Matplotlib** – para visualización de señales.
- **NumPy** – procesamiento numérico.
- **OpenCV** – procesamiento de imágenes.
- **Soundfile / SoundDevice** – manejo de audio.
- **Pillow** – manejo de imágenes en la GUI.
- **Pygame** – reproducción de audio.

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/pcm_modulation.git
cd pcm_modulation
