#ejercicio 1:
consumo = int(input("Ingrese el consumo: "))
habitantes = int(input("Ingrese el número de habitantes de la casa: "))

if consumo < 15:
    print(f"La tarifa es de: {consumo * 5}")
elif 15 <= consumo <= 30:  
    if habitantes > 3:
        print(f"La tarifa es de: {consumo * 4}")
    elif habitantes == 3:
        print(f"La tarifa de consumo es de: {consumo * 4}")
    else:
        print(f"La tarifa es de: {consumo * 5}")
else: 
    if habitantes > 5:
        print(f"La tarifa es de {consumo * 3.5}")
    elif habitantes % 2 == 0:
        print(f"La tarifa es de {consumo * 4}")
    else:
        print(f"La tarifa es de: {consumo * 4.2}")
        
#ejercio 2:
year = int(input("Ingrese el modelo del vehiculo: "))
placa = input("Ingrese su numero de placa: ")

digult = placa[-1]
digult = int(digult)
if year >= 2001:
    if digult % 2 == 0:
        print("El vehiculo no tiene permitido la circulacion los dias lunes. ")
    elif digult % 2 == 1: 
        print("El vehiculo no tiene permitido la circulacion los dias viernes.")
elif year < 2001:
    print("El vehiculo necesita mantenimiento obligatorio. ")
    if digult % 2 == 0:
        print("El vehiculo no tiene permitido la circulacion los dias lunes. ")
    elif digult % 2 == 1: 
        print("El vehiculo no tiene permitido la circulacion los dias viernes.")