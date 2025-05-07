myTuple = (45678, "Admin")
isActive=False

user = input("Ingrese user: ")
passWord = int(input("Ingrese contraseña: "))

if user == myTuple[1] and passWord == myTuple[0]:
    print("Bienvenido.")
else:
    print("Datos incorrectos.")