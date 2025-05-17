import numpy as np
import matplotlib.pyplot as plt

def MBPSK(bits):
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

    # Generamos la señal modulada BPSK
    for i, bit in enumerate(bits):
        if bit == 0:
            señal_modulada_completa[i * 100:(i + 1) * 100] = -np.sin(wc * t_continuo[i * 100:(i + 1) * 100])
        else:
            señal_modulada_completa[i * 100:(i + 1) * 100] = np.sin(wc * t_continuo[i * 100:(i + 1) * 100])

    # Graficamos la señal moduladora y la señal modulada BPSK
    #fig, ax = plt.figure(figsize=(12, 3))

    # Graficamos la señal moduladora (bits)
    #plt.subplot(2, 1, 1)
    #plt.step(np.arange(n_bits), bits, where='post', linewidth=2)
    #plt.title('Señal Moduladora (Bits)')
    #plt.ylim(-0.1, 1.1)  # Ajustamos el límite en y para mejor visualización
    #plt.xticks(np.arange(n_bits)+0.5, np.arange(1, n_bits + 1))  # Colocamos las etiquetas en el eje x
    #plt.ylabel('Amplitud')
    #plt.grid(True)

    # Graficamos la señal modulada BPSK
    #plt.subplot(2, 1, 2)
    plt.figure()
    plt.plot(t_continuo, señal_modulada_completa, linewidth=2)
    plt.title('Señal Modulada BPSK')
    plt.ylim(-1.5, 1.5)
    plt.xticks([])  # Eliminamos las etiquetas en el eje x
    plt.grid(True)

    # Etiquetamos cada bit en la señal modulada BPSK
    for i, bit in enumerate(bits):
        #Mostrar Baudios
        plt.text(i * T + T / 2, -1.2, str(i+1), ha='center')
        #Mostrar bits
        plt.text(i * T + T / 2, 1.2, str(bit), ha='center')
        plt.axvline(x=i * T, color='gray', linestyle='--')

    plt.tight_layout()
    #return ax
    plt.show()

