password="Python"
maxIntentos=3
isActive=False

userPass=input("Ingrese su contraseña: ")

while password != userPass:
    print("Contraseña incorrecta")
    maxIntentos-=1
    print(f"Tienes {maxIntentos} intentos")
    if maxIntentos==0:
        print("Usuario bloqueado")
        break
    userPass=input("Ingrese de nuevo su contraseña: ")

if password==userPass:    
    print("Contraseña correcta")
    isActive=True  

while isActive:
    for i in range (0,14):
        print(i)