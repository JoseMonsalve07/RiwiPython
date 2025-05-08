from GestionInventario2 import main
data=("Jose", 123)
print(f"Usuario: {data[0]}\nContraseña: {data[1]}")
user = input("Ingrese su usuario: ")
password = int(input("Ingrese su contraseña: "))

i=3
while i>1:
    i-=1
    if user == data[0] and password == data[1]:
        print("\n--- BIENVENIDO ---\n")
        main()
        break
    else:
        print(f"Contraseña y/o usuario incorrectos. le quedan {i} intentos.")
        user = input("Ingrese su usuario: ")
        password = int(input("Ingrese su contraseña: "))
        if i==0:
            break