password="Python"
intentos=0
maxIntentos=3

userPass=input("Ingrese su contraseña: ")

while password != userPass:
    print("Contraseña incorrecta")
    intentos+=1
    maxIntentos-=1
    print(f"Tienes {maxIntentos} intentos")
    if intentos == maxIntentos:
        print("Usuario bloqueado")
        break
    userPass=input("Ingrese de nuevo su contraseña: ")

if password==userPass:    
    print("Contraseña correcta")  