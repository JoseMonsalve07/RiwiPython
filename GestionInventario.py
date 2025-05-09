# Jose Manuel Bustamante Monsalve

inventory=[] # Se inicia una lista vacía para almacenar los productos

# Muestra el menú de opciones para interactuar con el inventario
def menu():
    print("\n--- BIENVENIDO ---\n")
    print("1. Ver inventario.")
    print("2. Añadir productos.")
    print("3. Consultar productos.")
    print("4. Actualizar precios.")
    print("5. Eliminar productos.")
    print("6. Calcular el valor total del inventario.")
    print("7. Salir.\n")

menu() # Se llama a la función menu para mostrar las opciones al usuario
option=int(input("Escoja una opción para interactuar con el inventario: "))


def emptyInventory():
        #Esta función imprime un mensaje indicando que el inventario está vacío.
        print("\nEl inventario está vacío.\n")

def seeInventory():
    #Esta función muestra la lista de productos en el inventario, incluyendo su nombre, precio y cantidad.
    i=0 # Se inicia un contador para enumerar los productos.
    print("Los productos en el inventario son los siguientes: \n")
    for product in inventory: # Se itera sobre cada producto en la lista inventory.
        i+=1 # Se incrementa el contador por cada producto que itere.
        print(f"Producto #{i}:\n Nombre: {product["Nombre"]}\n Precio: {product["Precio"]}\n Cantidad: {product["Cantidad"]}\n")

def addProduct():
    # Esta función permite al usuario añadir un nuevo producto al inventario, pidiendo su nombre, precio y cantidad.
    # El nuevo producto se almacena en la lista.
    
    list={} # Se crea un diccionario vacío para empezar a almacenar la información de cada producto.
    list["Nombre"]=input("Ingresa el nombre del producto: ") # Se pide el nombre del producto y se guarda en el diccionario con la clave "Nombre".
    list["Precio"]=float(input(f"Ingresa el precio de {list["Nombre"]}: ")) # Se pide el precio del producto, se convierte a float y se guarda con la clave "Precio".
    list["Cantidad"]=int(input(f"Ingresa la cantidad de {list["Nombre"]} disponible: ")) # Se pide la cantidad del producto, se convierte a int y se guarda con la clave "Cantidad".
    inventory.append(list) # Se añade el nuevo producto a la lista.
    print(f"El producto {list["Nombre"]} fue agregado con éxito\n")
    
def toContinue():
    # Esta función pregunta al usuario si desea volver al menú principal o salir del programa.
    global option
    print("¿Qué desea hacer a continuación?\n")
    print("1. Ver menú de opciones")
    print("2. Salir\n")
    option2=int(input("Ingrese una opción: "))
    if option2==1:
        menu() # Se llama a la función menu para mostrar las opciones otra vez.
        option=int(input("Escoja una opción para interactuar con el inventario: "))
    if option2==2:
        print("\n FIN \n")
        quit()    

def consultProduct():
    # Esta función permite al usuario buscar un producto en el inventario por su nombre y muestra su información si se encuentra.
    # Si el inventario está vacío, se llama a la función emptyInventory para indicarle al usuario que en el inventario no hay nada.
    if inventory:
        search=input("\nIngrese el nombre del producto: ")
        for product in inventory:
            if search==product["Nombre"]:
                print(f"\n Producto: {product["Nombre"]}\n Precio: {product["Precio"]}\n Cantidad: {product["Cantidad"]}\n")
                break # Se detiene la iteración una vez que se encuentra el producto.
        if search!=product["Nombre"]: # Se ejecuta si no se encuentra el producto.
            print(f"\nEl producto '{search}' no está en el inventario.\n")
    if not inventory:
        emptyInventory()
    
def updatePrice():
    # Esta función permite al usuario actualizar el precio de un producto en el inventario.
    # Primero muestra el inventario y luego pide el nombre del producto y el nuevo precio.
    # Si el inventario está vacío, se llama a la función emptyInventory para indicarle al usuario que en el inventario no hay nada.
    if inventory:
        seeInventory()
        toSelectProduct=input("Ingrese un producto del inventario (escrito de igual manera a como se ve en 'Nombre'): ")
        for product in inventory:
            if toSelectProduct==product["Nombre"]:
                toUpdatePrice=float(input("Ingrese el nuevo precio del producto: "))
                product["Precio"]=toUpdatePrice
                print(f"El nuevo precio de {product["Nombre"]} ahora es {product["Precio"]}\n")
                break
        if toSelectProduct!=product["Nombre"]:
                print(f"\nEl producto '{toSelectProduct}' no está en el inventario.\n")
                
    if not inventory:
        emptyInventory()

def deleteProduct():
    # Esta función permite al usuario eliminar un producto del inventario.
    # Primero muestra el inventario y luego pide el nombre del producto a eliminar.
    # Si el inventario está vacío, se llama a la función emptyInventory para indicarle al usuario que en el inventario no hay nada.
    if not inventory:
        emptyInventory()
    if inventory:
        print("\nLos productos en el invetario son los siguientes:\n")
        seeInventory()
        toSelectProduct=input("Ingrese el nombre del producto que será eliminado (escrito de igual manera a como se ve en 'Nombre'): ")
        for product in inventory:
            if toSelectProduct==product["Nombre"]:
                inventory.remove(product)
                print(f"El producto {toSelectProduct} fue eliminado del inventario.\n")
                break
        if toSelectProduct!=product["Nombre"]:
                print(f"\nEl producto '{toSelectProduct}' no está en el inventario.\n")

def inventoryTotalValue():
    # Esta función calcula y muestra el valor total del inventario, hace lo siguiente: suma de precio * cantidad de cada producto
    # Si el inventario está vacío, se llama a la función emptyInventory para indicarle al usuario que en el inventario no hay nada.
    if not inventory:
        emptyInventory()
    if inventory:
        totalValue=0 # Se crea una variable para guardar el valor total.
        for product in inventory:
            totalValue += product["Precio"] * product["Cantidad"]
        print(f"El valor total de los productos en el inventario es de {totalValue}")    

while True: # Bucle del programa que se ejecuta hasta que el usuario elige salir.
    
    if option < 1 or option > 7: # Valida que la opción ingresada esté entre 1-7
        option=int(input("Ingrese una opción valida: "))

    if option==1: # Si la opción seleccionada es 1 (Ver inventario).
        if len(inventory)==0: # Verifica que el inventario no esté vacío
            emptyInventory()
            toContinue()   
        else:
           seeInventory()
           toContinue()
        
    if option==2: # Si la opción seleccionada es 2 (Añadir productos).
        addProduct()
        toContinue()

    if option==3: # Si la opción seleccionada es 3 (Consultar productos).
        consultProduct()
        toContinue()

    if option==4: # Si la opción seleccionada es 4 (Actualizar precios).
        updatePrice()
        toContinue()
    
    if option==5: # Si la opción seleccionada es 5 (Eliminar productos).
        deleteProduct()
        toContinue()
    
    if option==6:  # Si la opción seleccionada es 6 (Calcular el valor total del inventario).
        inventoryTotalValue()
        toContinue()

    if option==7: # Si la opción seleccionada es 7 (Salir).
        print("\n FIN \n")
        break # Se rompe el bucle terminando el programa.