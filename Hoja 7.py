#ejercicio 1
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

#ejercicio 2
x = 1
while x < 11:
    if x % 2 ==1:
        print(x)
    x += 1

#escenario 1
while True:
    palabra = input("Ingresa la palabra secreta: ")
    if palabra == "chupacabra":
        print("Has dejado el bucle con exito")
        break

#escenario 3
palabra = input("Ingrese una palabra: ")
palabra = palabra.upper()
for letra in palabra:
    if letra in "AEIOU":
        continue
    print(letra)