#Programa que extraiga la primera y la última palabra de una oración
texto1= "Python es un lenguaje poderoso y usable hola que tal "
palabra1= texto1.split()
numpalab = len(palabra1)
print(palabra1[0]), print(palabra1[-1])

#Programa que elimine los espacios repetidos en una cadena
texto2 = "Hola   mundo   en   Python  Sebastian   Yi   Pi   Ti"
palabra2 = texto2.split()
fraseespa =" ".join(palabra2)
print(fraseespa)

#Dado un correo electrónico, extrae solo el dominio.
texto3 = "usuario@yahooogmail.com"
palabra3 = texto3.split("@")
dominio = len(palabra3)
print(palabra3[-1])

#Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf)
texto4 = "documento.pdf"
resultadotrue = texto4.endswith(".pdf",)
print(resultadotrue)

#Dado un texto, invierte el orden de las palabras
texto5 = "Me gusta Python"
alreves = " ".join(texto5.split()[::-1])
print(alreves)

#Dado un texto ingresado por el usuario detectar palabras claves y responder
soli = input("")
cadenasoli = soli.split()
poemaamor = "El susurro del viento me llama, lleva tu nombre en su brisa calma. La luna brilla, cómplice del querer, en su luz veo tu alma renacer."
poemamelan = "En la penumbra del recuerdo me hallo, voces lejanas cantan un triste fallo. El tiempo, verdugo sin compasión, deja cicatrices en mi corazón."
poemasol = "La noche abraza mi ser entero, un eco vacío, frío y severo. Las estrellas, mi única compañía, bailan mudas en la lejanía."
poemasup = "Del abismo oscuro logro alzarme, cada herida me enseña a levantarme. El fuego en mi pecho vuelve a encender, soy más fuerte tras cada caer."
poematra = "Un puñal de hielo cruza el pecho, promesas rotas en un cruel despecho. Pero la verdad renace al final, un alma libre no teme el mal."

if("amor" in cadenasoli):
    print(poemaamor)
elif("melancolia" in cadenasoli):
    print(poemamelan)
elif("soledad" in cadenasoli):
    print(poemasol)
elif("superacion" in cadenasoli):
    print(poemasup)
elif("traicion" in cadenasoli):
    print(poematra)
else: 
    print("No hay poemas disponibles para tu petición.")