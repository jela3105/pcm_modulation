import numpy as np
import matplotlib.pyplot as plt

# Definimos las ecuaciones de salida para cada combinación de bits (Q, I, C)
def ecuacion_salida(Q, I, C, wc, t):
    if Q == 0:
        signo_cos = -1
    else:
        signo_cos = 1
     
    if I == 0:
        signo_sen = -1
    else:
        signo_sen = 1
        
    if C == 0:
        sen_coef = 0.541
        cos_coef = 1.307
    else:
        sen_coef = 1.307
        cos_coef = 0.541
        
    return signo_cos * cos_coef * np.cos(wc * t) + signo_sen * sen_coef * np.sin(wc * t)

def M8PSK(bits):
    # Longitud de la señal en bits
    n_bits = len(bits)

    # Frecuencia de la onda portadora en baudios
    baud_rate = 7
    # Tiempo de símbolo (periodo de la onda portadora)
    T = 1 / baud_rate
    # Tiempo total de la señal
    tiempo_total = n_bits * T
    # Generamos el tiempo continuo para la onda portadora
    t_continuo = np.linspace(0, tiempo_total, 100 * n_bits)
    # Frecuencia de la onda portadora
    wc = 2 * np.pi * baud_rate

    # Preparamos el arreglo para la señal modulada completa
    señal_modulada_completa = np.zeros_like(t_continuo)



    # Generamos la señal modulada 8PSK
    for i in range(n_bits // 3):
        Q = bits[i * 3]
        I = bits[i * 3 + 1]
        C = bits[i * 3 + 2]
        
        # Generamos la señal modulada para este grupo de 3 bits
        señal_modulada_completa[i * 300:(i + 1) * 300] = ecuacion_salida(Q, I, C, wc, t_continuo[i * 300:(i + 1) * 300])

    # Graficamos la señal moduladora y la señal modulada 8PSK
    #plt.figure(figsize=(10, 8))

    # Graficamos la señal moduladora (bits)
    #plt.subplot(2, 1, 1)
    #plt.step(np.arange(n_bits), bits, where='post', linewidth=2)
    #plt.title('Señal Moduladora (Bits)')
    #plt.ylim(-0.1, 1.1)  # Ajustamos el límite en y para mejor visualización
    #plt.xticks(np.arange(n_bits)+0.5, np.arange(1, n_bits + 1))  # Colocamos las etiquetas en el eje x
    #plt.ylabel('Amplitud')
    #plt.grid(True)

    # Graficamos la señal modulada 8PSK
    #plt.subplot(2, 1, 2)
    plt.figure()
    plt.plot(t_continuo, señal_modulada_completa, linewidth=2)
    plt.title('Señal Modulada 8PSK')
    plt.ylim(-1.5, 1.5)
    plt.xticks([])  # Eliminamos las etiquetas en el eje x
    plt.grid(True)

    # Etiquetamos cada grupo de 3 bits en la señal modulada 8PSK
    for i in range(n_bits // 3):
        #Mostrar Baudios
        plt.text(i * 3 * T + 1.5 * T, -1.2, str(i+1), ha='center')
        #Mostrar bits
        plt.text(i * 3 * T + 1.5 * T, 1.2, f'{bits[i * 3]}{bits[i * 3 + 1]}{bits[i * 3 + 2]}', ha='center')
        plt.axvline(x=i * 3 * T, color='gray', linestyle='--')

    plt.tight_layout()
    plt.show()