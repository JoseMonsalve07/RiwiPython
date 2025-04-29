Age=int(input("Ingrese su edad "))

if Age < 12:
    print("Eres un niño")
if Age >= 12 and Age <= 17:
    print("Eres un adolescente")
if Age >= 18 and Age <= 59:
    print("Eres un adulto")
if Age >= 60:
    print("Eres un adulto mayor")    