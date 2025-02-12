num= int(input("Ingrese un numero del 1 al 9: "))

if num >= 1 and num <=9:
    if num <= 3: 
        resultado = num * "I"
        print(f"El número {num} en numeros Romanos es: {resultado}")
    if num == 4:
        print(f"El número {num} en números Romanos es: IV")
    if num >= 5 and num <= 8:
        resultado = "V"+(num - 5)*"I"
        print(f"El número {num} en números Romanos es: {resultado}")
    if num == 9:
        print(f"El número {num} en números Romanos es: IX")
elif num > 9 or num <= 0:
    print("El número es inválido")
