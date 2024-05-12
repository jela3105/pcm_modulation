import numpy as np

class cuantizacion:

    def __init__(self, n, data) -> None:
        self.DR = self.calculo_DR(n)
        self.resolucion = np.amax(data)/self.DR

    def calculo_DR(self, n):
        return (2**n) - 1
    
    def imprimir_valores(self):
        print("DR: ", self.DR)
        print("Resolucion: ", self.resolucion)