import numpy as np
import matplotlib.pyplot as plt
def decode_and_amplitude(bits):
    amplitudes = []
    for i in range(0, len(bits), 4):
        Q = bits[i]
        Q_inverso = bits[i + 1]
        I = bits[i + 2]
        I_inverso = bits[i + 3]
            
        signo_cos = 1 if Q == 1 else -1
        signo_sen = 1 if I == 1 else -1
        magnitud_cos = 0.821 if Q_inverso == 1 else 0.22
        magnitud_sen = 0.821 if I_inverso == 1 else 0.22
            
        amplitude = np.sqrt(magnitud_cos**2 + magnitud_sen**2)
        amplitudes.append(amplitude)
        
    return amplitudes



def M16QAM(bits):
    n_bits = len(bits)
    baud_rate = 1  # Ajustamos la frecuencia de baudios a 1 para que cada símbolo ocupe el espacio necesario
    T = 1 / baud_rate
    tiempo_total = n_bits / 4 * T  # Ajustamos el tiempo total basado en el número de símbolos (cada símbolo = 4 bits)
    t_continuo = np.linspace(0, tiempo_total, 100 * (n_bits // 4))
    wc = 2 * np.pi * baud_rate

    señal_modulada_completa = np.zeros_like(t_continuo)

    amplitudes = decode_and_amplitude(bits)

    for i in range(len(bits) // 4):
        amplitude = amplitudes[i]
        Q = bits[i * 4]
        Q_inverso = bits[i * 4 + 1]
        I = bits[i * 4 + 2]
        I_inverso = bits[i * 4 + 3]
        
        signo_cos = 1 if Q == 1 else -1
        signo_sen = 1 if I == 1 else -1
        magnitud_cos = 0.821 if Q_inverso == 1 else 0.22
        magnitud_sen = 0.821 if I_inverso == 1 else 0.22
        
        señal_modulada_completa[i * 100:(i + 1) * 100] = amplitude * (magnitud_cos * np.cos(wc * t_continuo[i * 100:(i + 1) * 100]) * signo_cos + magnitud_sen * np.sin(wc * t_continuo[i * 100:(i + 1) * 100]) * signo_sen)

    plt.figure()

    #plt.subplot(2, 1, 1)
    #plt.step(np.arange(n_bits), bits, where='post', linewidth=2)
    #plt.title('Señal Moduladora (Bits)')
    #plt.ylim(-0.1, 1.1)
    #plt.xticks(np.arange(n_bits)+0.5, np.arange(1, n_bits + 1))
    #plt.ylabel('Amplitud')
    #plt.grid(True)

    #plt.subplot(2, 1, 2)
    plt.plot(t_continuo, señal_modulada_completa, linewidth=2)
    plt.title('Señal Modulada 16QAM')
    plt.ylim(-1.5, 1.5)
    plt.xlim(0, tiempo_total)  # Ajustamos el límite en x para que ocupe todo el espacio
    plt.xlabel('Tiempo')
    plt.grid(True)

    for i in range(len(bits) // 4):
        plt.text(i * T + T / 2, -1.2, str(i + 1), ha='center')
        plt.text(i * T + T / 2, 1.2, f'{bits[i * 4]}{bits[i * 4 + 1]}{bits[i * 4 + 2]}{bits[i * 4 + 3]}', ha='center')
        plt.axvline(x=i * T, color='gray', linestyle='--')

    plt.tight_layout()
    plt.show()

