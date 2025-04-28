def dolar(y):
    convert=y*4000
    return f"su salario en pesos es: {convert}"
def peso(y):
    convert=y/4000
    print( )
    return f"Su salario en dolares es: {convert}"

x=str(input("Gana en USD o COP "))
y=float(input("Ingrese su salario "))

if x == "USD":
    aa=dolar(y)
    print(aa)

if x == "COP":
    bb=peso(y)
    print(bb)