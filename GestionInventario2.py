# Jose Manuel Bustamante Monsalve
inventory=[]

def menu():
    print("\n--- BIENVENIDO ---\n")
    print("1. Ver inventario.")
    print("2. Añadir productos.")
    print("3. Consultar productos.")
    print("4. Actualizar precios.")
    print("5. Eliminar productos.")
    print("6. Calcular el valor total del inventario.")
    print("7. Salir.\n")
menu()
option=int(input("Escoja una opción para interactuar con el inventario: "))


def emptyInventory():
        print("\nEl inventario está vacío.\n")

def seeInventory():
    i=0
    for product in inventory:
        i+=1
        print(f"Producto #{i}:\n Nombre:{product["Nombre"]}\n Precio:{product["Precio"]}\n Cantidad:{product["Cantidad"]}\n")

def addProduct():
    list={}
    list["Nombre"]=input("Ingresa el nombre del producto: ")
    list["Precio"]=float(input(f"Ingresa el precio de {list["Nombre"]}: "))
    list["Cantidad"]=int(input(f"Ingresa la cantidad de {list["Nombre"]} disponible: "))
    print(f"El producto {list["Nombre"]} fue agregado con éxito\n")
    inventory.append(list)

def toContinue():
    global option
    print("¿Qué desea hacer a continuación?\n")
    print("1. Ver menú de opciones")
    print("2. Salir\n")
    option2=int(input("Ingrese una opción: "))
    if option2==1:
        menu()
        option=int(input("Escoja una opción para interactuar con el inventario: "))
    if option2==2:
        quit()    

def consultProduct():
    search=input("\nIngrese el nombre del producto:")
    for product in inventory:
        if product["Nombre"]==search:
            print(f"\n Producto: {product["Nombre"]}\n Precio:{product["Precio"]}\n Cantidad:{product["Cantidad"]}\n")
        if product["Nombre"]!=search:
            print(f"\nEl producto '{search}' no está en el inventario.\n")
    if not inventory:
            emptyInventory()

while True:
    if option==1:
        if len(inventory)==0:
            emptyInventory()
            toContinue()
            continue    
        else:
           seeInventory()
           toContinue()
        
    if option==2:
        addProduct()
        toContinue()

    if option==3:
        consultProduct()
        toContinue()

    if option==7:
        break