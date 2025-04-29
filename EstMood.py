#lista
frutas = ["Pera", "Manzana", "Guayaba"]

for fruta in frutas:
    print(fruta)

#tupla
ciudades = ["madrid", "barcelona", "valencia"]

for ciudad in ciudades:
    print(ciudad)

#cadena de caracteres
mensaje = "Hola"

for caracter in mensaje:
    print(caracter)

# Ejemplo de un ciclo for con una cadena de caracteres
numeros=[3, 8, 15, 1, 22, 7, 18]
umbral=10

for numero in numeros:
    if numero > umbral:
        print(f"El primer numero mayor que {umbral} es {numero}.")
        break
else:
    print(f"Ningun numero en la lista es mayor que {umbral}")

# Ejemplo de un ciclo while con una cadena de caracteres

while True:
    texto=input("Escribe algo(o 'salir' para terminar): ")

    if texto=="salir":
        print("Adios")
        break
    print(f"Escribiste: {texto}")

# Continue. Si el número es impar, salta al siguiente ciclo evitando que se imprima

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"Número: {numero}")