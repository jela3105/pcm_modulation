import numpy as np

class cuantizacion:

    def __init__(self, n, data, es_imagen) -> None:
        self.data = data
        self.n = n
        self.es_imagen = es_imagen
        self.DR = self.calculo_DR(n)
        self.resolucion = np.amax(data)/self.DR
        self.variacion_rango = self.resolucion/2
        self.tabla_codigo = self.crear_tabla_codigo()

    def calculo_DR(self, n):
        return (2**n) - 1
    
    def imprimir_valores(self):
        print("DR: ", self.DR)
        print("Resolucion: ", self.resolucion)
        print("Tabla codigo: ", self.tabla_codigo)

    def crear_tabla_codigo(self):
        #arreglo tiene(bit signo, nivel cuantizacion, voltaje_cuantizacion, rango_minimo, rango_max)
        tabla_codigo = []
        for x in range(self.DR + 1):
            voltaje_cuantizacion = x * self.resolucion
            minimo_rango = voltaje_cuantizacion - self.variacion_rango
            maximo_rango = voltaje_cuantizacion + self.variacion_rango 
            tabla_codigo.append((1, x, voltaje_cuantizacion, minimo_rango, maximo_rango))
            if not self.es_imagen:
                tabla_codigo.insert(0, (0, x, voltaje_cuantizacion * -1, maximo_rango * -1, minimo_rango * -1))
        
        return tabla_codigo
    
    def decimal_a_binario(self, numero):
        binario = ""
        while numero > 0:
            residuo = numero % 2
            binario = str(int(residuo)) + binario
            numero //= 2

        while len(binario) < self.n:
            binario = "0" + binario

        return binario

    def recuantizar_data(self):
        if not self.es_imagen:
            data_recuantizada = []
            binario = ""
            for x in self.data:
                numero_cuantizacion = x // self.resolucion
                residuo = x % self.resolucion
                if residuo >= self.variacion_rango:
                    numero_cuantizacion = numero_cuantizacion + 1
                data_recuantizada.append(numero_cuantizacion * self.resolucion)
                if x < 0:
                    binario = binario + "0" + self.decimal_a_binario(numero_cuantizacion)
                else:
                    binario = binario + "1" + self.decimal_a_binario(numero_cuantizacion)

            with open("audio_codigo_pcm.txt", "w") as archivo:
                archivo.write(binario)

            print(len(set(data_recuantizada)))
            return data_recuantizada
        else:
            data_recuantizada = np.copy(self.data)
            binario = ""
            for i, x in enumerate(self.data):
                for j, y in enumerate(self.data[i]):

                    numero_cuantizacion = self.data[i][j] // self.resolucion
                    residuo = self.data[i][j] % self.resolucion
                    if residuo >= self.variacion_rango:
                        numero_cuantizacion = numero_cuantizacion + 1

                    data_recuantizada[i][j] = numero_cuantizacion * self.resolucion
                    binario = binario + self.decimal_a_binario(numero_cuantizacion)

            print("binario", self.decimal_a_binario(2))
            with open("imagen_codigo_pcm.txt", "w") as archivo:
                archivo.write(binario)
            print("imagen recuantizada", data_recuantizada)
            return data_recuantizada 