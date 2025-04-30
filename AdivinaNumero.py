import random
aleatoryNumber=random.randint(1, 10)
print(aleatoryNumber) 
userAnswer=int(input("Hay un número aleatorio de 0 a 10. Ingrese un número hasta que lo adivine: "))

while userAnswer != aleatoryNumber:
    userAnswer=int(input("Hay un número aleatorio de 0 a 10. Ingrese un número hasta que lo adivine: "))
    while userAnswer < 0 or userAnswer > 10:
        userAnswer=int(input("Ingrese un numero válido. Solo numeros entre 0 y 10: ")) 
if userAnswer == aleatoryNumber:
        print("Correcto. Ha adivinado el numero.")
   