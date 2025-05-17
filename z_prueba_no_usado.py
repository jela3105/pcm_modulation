import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_baud = 7  # Número de baudios
baud_rate = 1  # Tasa de baudios (símbolos por segundo)
fs = 100  # Frecuencia de muestreo (muestras por segundo)
carrier_freq = 5  # Frecuencia de la portadora (ejemplo: 5 Hz)

# Mapeo de bits a símbolos 16-QAM
def bits_to_16qam(bits):
    # Constelación 16-QAM
    constellation = {
        '0000': {'symbol': -1-1j, 'phase_deg': -135}, '1000': {'symbol': -1+1j, 'phase_deg': 135},
        '0001': {'symbol': -3-1j, 'phase_deg': -165}, '1001': {'symbol': -3+1j, 'phase_deg': 165},
        '0010': {'symbol': 1-1j, 'phase_deg': -45}, '1010': {'symbol': 1+1j, 'phase_deg': 45},
        '0011': {'symbol': .821-.22j, 'phase_deg': -90}, '1011': {'symbol': 3+1j, 'phase_deg': 15},
        '0100': {'symbol':  .821-.22j, 'phase_deg': -65}, '1100': {'symbol':  -1+3j, 'phase_deg': 105},
        '0101': {'symbol':  -3-3j, 'phase_deg': -135}, '1101': {'symbol':  -3+3j, 'phase_deg': 135},
        '0110': {'symbol':  1-3j, 'phase_deg': -75}, '1110': {'symbol':  1-3j, 'phase_deg': 75},
        '0111': {'symbol':  3-3j, 'phase_deg': -45}, '1111': {'symbol':  3+3j, 'phase_deg': 45}
    }
    symbols = []
    phases = []
    for i in range(0, len(bits), 4):
        bit_group = bits[i:i+4]
        symbol = constellation.get(bit_group, {'symbol': 0})['symbol']
        phase_deg = constellation.get(bit_group, {'phase_deg': 0})['phase_deg']
        symbols.append(symbol)
        phases.append(phase_deg)
    return np.array(symbols), phases

# Definir la secuencia binaria (28 bits para 7 baudios)
binary_sequence = '0011010010100110110111001111'  # 28 bits

# Asegurarse de que la longitud de la secuencia binaria es correcta
assert len(binary_sequence) == num_baud * 4, "La longitud de la secuencia binaria debe ser múltiplo de 4 y coincidir con el número de baudios."

# Convertir la secuencia binaria a símbolos 16-QAM y obtener las fases
symbols, phases = bits_to_16qam(binary_sequence)

# Generar la señal en tiempo discreto
t_symbol = 1 / baud_rate  # Duración de cada símbolo en segundos
t = np.arange(0, num_baud * t_symbol, 1 / fs)  # Vector de tiempo total
signal = np.zeros_like(t, dtype=complex)

# Generar la señal modulada
for i, symbol in enumerate(symbols):
    # Definir el tiempo de inicio y fin de cada símbolo
    t_start = i * t_symbol
    t_end = (i + 1) * t_symbol
    symbol_phase_rad = np.deg2rad(phases[i])  # Convertir la fase a radianes
    #symbol_phase_rad=(symbol_phase_rad*3.1416)*180
    carrier = np.exp(1j * (2 * np.pi * carrier_freq * t +symbol_phase_rad))
    signal[int(t_start * fs):int(t_end * fs)] = symbol * carrier[int(t_start * fs):int(t_end * fs)]

# Señal modulada
modulated_signal = np.real(signal)

# Graficar las señales
plt.figure(figsize=(14, 8))

# Graficar la señal moduladora
plt.subplot(2, 1, 1)
plt.plot(t, np.real(signal), label='I (In-phase)')
plt.plot(t, np.imag(signal), label='Q (Quadrature)')
plt.title('Señal Moduladora 16-QAM')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

# Graficar la señal modulada
plt.subplot(2, 1, 2)
plt.plot(t, modulated_signal, label='Señal Modulada')
plt.title('Señal Modulada 16-QAM')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()