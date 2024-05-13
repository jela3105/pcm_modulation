import numpy as np

class cuantizacion:

    def __init__(self, n, data, es_imagen) -> None:
        self.data = data
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
        #arreglo tiene(bit signo, codigo binario, voltaje_cuantizacion, rango_minimo, rango_max)
        tabla_codigo = []
        for x in range(self.DR + 1):
            voltaje_cuantizacion = x * self.resolucion
            minimo_rango = voltaje_cuantizacion - self.variacion_rango
            maximo_rango = voltaje_cuantizacion + self.variacion_rango 
            tabla_codigo.append((1, x, voltaje_cuantizacion, minimo_rango, maximo_rango))
            if not self.es_imagen:
                tabla_codigo.insert(0, (0, x, voltaje_cuantizacion * -1, maximo_rango * -1, minimo_rango * -1))
        
        return tabla_codigo

    def recuantizar_data(self):
        if not self.es_imagen:
            data_recuantizada = []
            for x in self.data:
                numero_cuantizacion = x / self.resolucion
                residuo = x % self.resolucion
                if residuo >= self.variacion_rango:
                    numero_cuantizacion = numero_cuantizacion + 1
                data_recuantizada.append(numero_cuantizacion * self.resolucion)
            print(len(set(data_recuantizada)))
            return data_recuantizada
        else:
            return self.data 