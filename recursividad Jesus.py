# Ejercicio 1
def es_par_o_impar(n):
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")
es_par_o_impar(3)

#ejercicio 2
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
print(suma_lista([1, 2, 3]))  

#ejercicio 3
def cuenta_regresiva(n):
    if n < 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)
cuenta_regresiva(3)

#ejercicio 4
def cuenta_ascendente(n, actual=1):
    if actual > n:
        return
    else:
        print(actual)
        cuenta_ascendente(n, actual + 1)
cuenta_ascendente(5)

#ejercicio 5
def suma_hasta(n):
    if n == 0:
        return 0
    return n + suma_hasta(n - 1)
print(suma_hasta(4))

#ejercicio 6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#ejercicio 7
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        menor_del_resto = minimo(lista[1:])
        return lista[0] if lista[0] < menor_del_resto else menor_del_resto

# Juego
import time

def adivina_el_numero(numero, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Se acabaron los intentos! El número era:", numero)
        return
    intento = int(input("Ingresa tu intento: "))
    if intento == numero:
        tiempo_total = time.time() - tiempo_inicio
        print("¡Adivinaste el número!")
        print(f"Tiempo total: {tiempo_total} segundos")
    elif intento < numero:
        print("El número es mayor")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)
    else:
        print("El número es menor")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)
print(minimo([5, 3, 8, 1, 2])) 