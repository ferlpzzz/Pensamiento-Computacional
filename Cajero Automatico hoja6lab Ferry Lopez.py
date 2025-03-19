saldo = 3000
contador = 0
print(f"Saldo disponible: Q{saldo}")
while True:
    retiro = input("Ingrese el monto a retirar: ")
    if retiro == "0":
        print("Gracias por usar el cajero.")
        break
    retiro = int(retiro)
    if retiro > saldo:
        contador += 1
        print(f"Saldo insuficiente. Intentos restantes: {3 - contador}")
        if contador >= 3: 
            print("Demasiados intentos fallidos. Cerrando cajero automatico...")
            break
    else: 
        saldo -= retiro
        print(f"Retiro exitoso. Nuevo saldo disponible: Q{saldo}")
        if saldo == 0: 
            print("Saldo agotado. Nos vemos a la proxima...")
            break
