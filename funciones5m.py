def doble(x):
    valor=x*2
    return valor
print(doble(3))

print("--------------------------------------------------")

def hello(name, lastName):
    print("Hola", name,lastName)

hello("Jose", "Monsalve")

print("--------------------------------------------------")

def helloo(name, lastName):
    print("Hola", name,lastName)
    pi=3,1416
    print(pi)
    return ("Hola", name,lastName, "desde return")

result = helloo("Jose", "Manuel")
print(result)

print("--------------------------------------------------")

def multiplicar(a, b):
    resultado=a*b
    name="Esteban"
    print(name)
    print("1")
    print("4")
    return resultado

print("2")
productValue=multiplicar(2,8)
print("3")
print(productValue)

print(multiplicar(20,60))

print("--------------------------------------------------")

def multiplicarSuma(a, b, x, y):
    resultadoM= a*b
    resultadoS= x+y
    return resultadoM, resultadoS

productM, productS=multiplicarSuma(2,8,4,4)
print(productM)
print(productS)