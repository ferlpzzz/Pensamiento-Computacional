#ejercicio 1 
from abc import ABC, abstractmethod

class ExperimentoFisico(ABC):
    @abstractmethod
    def realizar_experimento(self):
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad=9.81):
        self.altura = altura
        self.gravedad = gravedad
        
    def calcular_tiempo_caida(self):
        if self.altura < 0:
            raise ValueError("La altura no puede ser negativa")
        if self.gravedad <= 0:
            raise ValueError("La gravedad debe ser mayor que cero")
        
        tiempo = (2 * self.altura / self.gravedad) ** 0.5
        return tiempo
    
    def realizar_experimento(self):
        try:
            tiempo = self.calcular_tiempo_caida()
            print(f"El tiempo de caída desde {self.altura} metros es {tiempo:.2f} segundos")
            return tiempo
        except ValueError as e:
            print(f"Error en el experimento: {e}")
            return None

if __name__ == "__main__":
    print("=== Simulación de Caída Libre ===")
    
    experimento1 = CaidaLibre(altura=10)
    experimento1.realizar_experimento()
    
    experimento2 = CaidaLibre(altura=45)
    experimento2.realizar_experimento()
    
    experimento3 = CaidaLibre(altura=2, gravedad=1.62)
    experimento3.realizar_experimento()
    
    experimento4 = CaidaLibre(altura=-5)
    experimento4.realizar_experimento()
    
    experimento5 = CaidaLibre(altura=10, gravedad=0)
    experimento5.realizar_experimento()
    
#ejercicio 2
import math

class OperacionCientifica(ABC):
    @abstractmethod
    def calcular(self, *args):
        pass

class RaizCuadrada(OperacionCientifica):
    def calcular(self, numero):
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(numero)

class Potencia(OperacionCientifica):
    def calcular(self, base, exponente):
        return math.pow(base, exponente)

class Logaritmo(OperacionCientifica):
    def calcular(self, numero, base=math.e):
        if numero <= 0:
            raise ValueError("El número debe ser positivo para calcular el logaritmo")
        if base <= 0 or base == 1:
            raise ValueError("La base del logaritmo debe ser positiva y diferente de 1")
        return math.log(numero, base)

class Factorial(OperacionCientifica):
    def calcular(self, numero):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("El factorial solo está definido para enteros no negativos")
        return math.factorial(numero)

if __name__ == "__main__":
    try:
        raiz = RaizCuadrada()
        print("Raíz cuadrada de 16:", raiz.calcular(16))
        
        potencia = Potencia()
        print("2 elevado a 3:", potencia.calcular(2, 3))
        
        log = Logaritmo()
        print("Logaritmo natural de 10:", log.calcular(10))
        
        fact = Factorial()
        print("Factorial de 5:", fact.calcular(5))
        
    except ValueError as e:
        print("Error:", e)