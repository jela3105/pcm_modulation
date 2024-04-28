import cv2
import matplotlib.pyplot as plt  

# Función para convertir una imagen a escala de grises
def convertir_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return imagen_gris

# Función para binarizar una imagen
def binarizar_imagen(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para binarizar la imagen
    _, imagen_binarizada = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)
    
    return imagen_binarizada

def main():
    # Ruta de la imagen a leer
    ruta_imagen = "imagen2.jpg"

    # Leer la imagen
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se ha leído correctamente
    if imagen is None:
        print("Imagen no encontrada")
        return

    # Binarizar la imagen
    imagen_binarizada = binarizar_imagen(imagen)

    # Convertir la imagen a escala de grises
    imagen_gris = convertir_a_grises(imagen)
            
    plt.figure(figsize=(12, 4))
        
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')
        
    plt.subplot(132)
    plt.imshow(imagen_gris, cmap='gray')
    plt.title('Imagen Escala de Grises')
    plt.axis('off')
        
    plt.subplot(133)
    plt.imshow(imagen_binarizada, cmap='binary')
    plt.title('Imagen Binarizada')
    plt.axis('off')
      
    plt.show()
         
    # Esperar a que se presione una tecla y luego cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("hola mundo")
if __name__ == "__main__":
    main()