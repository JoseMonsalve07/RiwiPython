def sumar(x, y):
    result=x+y
    return result
print(sumar(50,60))

sumarLambda= lambda x, y: x + y
print(sumarLambda(10,12))

lista=[2,4,8,10]
averageLambda= lambda x: sum(x)/len(x)
print(averageLambda(lista))