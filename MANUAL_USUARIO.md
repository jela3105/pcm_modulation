# Manual de Usuario – PCM Modulation Interface

Este manual guía al usuario en el uso de la interfaz gráfica desarrollada para la cuantización y modulación digital de señales PCM, ya sea en formato de imagen o audio.

## 1. Inicio de la Aplicación

Para ejecutar la aplicación, utiliza:

```bash
python main.py
```

## 2.- Imagen Binarizada

Se muestra interfaz donde se mueestra:

Imagen original a color.

Imagen en escala de grises.

Imagen binarizada (0 y 1).

Esto permite visualizar cómo se realiza el preprocesamiento antes de la cuantización.

Al apretar el boton "Ir a Interfaz PCM" lo llevara a otra interfaz

## 3. Interfaz PCM

Se mostrará una interfaz gráfica con varias secciones:

Seccion de Audio

Seccion de Imagen

Seccion de Grabacion de audio

Dropdown de Niveles de Cuantización: Selecciona la cantidad de niveles para la cuantización (1 a 8).

Visualización: Se muestra la imagen original y la cuantizada o botones de audio.

## 5. Uso con Imágenes
Selecciona "Imagen" en el primer dropdown.

Elige un número de niveles de cuantización.

Observa los cambios en la imagen cuantizada.

## 6. Uso con Audio
Selecciona "Audio" en el primer dropdown.

Elige un número de niveles de cuantización.

Usa los botones para reproducir el audio original y recuantizado.

## 4.Interfaz Graficacion
La interfaz incluye dos botones principales:

Mostrar gráfica código binario: Abre una ventana con la representación binaria de la señal PCM.

Mostrar gráfica de modulación: Abre una ventana con la señal modulada según la técnica seleccionada.

En ella se escogera entre Imagen y audio son su nivel de cuantizacion y una de estas tres tecnicas

BPSK, 8PSK y 16QAM

y con los botones antes mencionados se mostrara su grafica

## 8. Recomendaciones
Asegúrate de tener los archivos necesarios:

audio/audio_mono.wav

images/imagen_gris.jpg

images/imagen_cuantizada.jpg

Ejecuta con Python 3.11 o superior.

Instala las dependencias si es la primera vez que corres el programa:

pip install -r requirements.txt


