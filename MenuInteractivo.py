print("Bienvenido! Elige una opción:")
print("")
print("Saludar")
print("Decir tu edad")
print("Salir")
print("")
Answer=input("")

while Answer != "salir":
    if Answer == "saludar":
        print("Hola Usuario!")
        break
    if Answer == "decir tu edad":
        Age=input("Ingresa tu edad: ")
        while not Age.isnumeric():
            Age=input("Ingresa una edad válida: ")
        print(f"Usuario, tu edad es: {Age}")
        break    

if Answer == "salir":
    print("Adios Usuario")
