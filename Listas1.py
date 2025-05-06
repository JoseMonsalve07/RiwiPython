# imprimir dato por posición

lista = [7, "hola", True, 3.5]
print(lista)
print(lista[2])

# agregar dato a la lista en cierta posición

lista.insert(2, 'manzana')
print(lista)

# agregar dato a la lista al final

lista.append("celular")
print(lista)

#agregar una lista a otra

lista2= ["celular", "billetera"]
lista.extend(lista2)
print(lista)

# eliminar datos por posición

lista3=["hola", "como", "estas"]
del lista3[2]
print(lista3)

# eliminar dato especifico

lista3=["hola", "como", "estas"]
lista3.remove("hola")
print(lista3)

# eliminar todo el contenido de una lista

lista3=["hola", "como", "estas"]
print(lista3)
lista3.clear()
print(lista3)

# eliminar elemento de la lista

lista4=["casa", "zapato", "manzana"]
objt_eliminado=lista4.pop(1)
# si esta vacío el índice, eliminará el último
print(lista4)
print(objt_eliminado)

# tomar un segmento de la lista

lista5=["casa", "zapato", "manzana", 8, 4]
print(lista5)
print(lista5[1:3])

# iterar una lista o imprimir todo

lista = [7, "hola", True, 3.5]
for objetos in lista:
    print(objetos)

# ordenar de menor a mayor
listaN=[0.5, 1, 4, 6, 3.5, 2]
print(listaN)
listaN.sort()
print(listaN)    