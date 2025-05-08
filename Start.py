from GestionInventario2 import main
data=("Jose", 123)
print(f"Usuario: {data[0]}\nContraseña: {data[1]}")
isActive=False

user = input("Ingrese su usuario: ")
password = int(input("Ingrese su contraseña: "))

if user == data[0] and password == data[1]:
    print("\n--- BIENVENIDO ---\n")
    main()

while user != data[0] or password != data[1]:
    isActive=False
    while isActive==False:
        print(f"Contraseña y/o usuario incorrectos.")
        user = input("Ingrese su usuario: ")
        password = int(input("Ingrese su contraseña: "))
        if user == data[0] and password == data[1]:
            isActive=True
           
    if isActive==True:
        print("\n--- BIENVENIDO ---\n")
        main()
        break
            

