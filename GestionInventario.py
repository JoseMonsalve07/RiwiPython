# Jose Manuel Bustamante Monsalve
# Actividad: Gestión de inventarios con funciones y colecciones.


print("")
print("--- BIENVENIDO ---")
print("")
print("1. Ver inventario.")
print("2. Añadir productos.")
print("3. Consultar productos.")
print("4. Actualizar precios.")
print("5. Eliminar productos.")
print("6. Calcular el valor total del inventario.")
print("")
option=int(input("Escoja una opción para interactuar con el inventario: "))
print("")
inventory={}
products={}
while True:
    while option<1 or option>6:
        option=int(input("Escoja una opción válida: "))

    if option==1:
        if len(inventory)==0:
            print("El inventario está vacío.")
            print("")
            print("1. Ver menú de opciones")
            print("2. Salir")
            print("")
            option2=int(input(""))
            if option2==1:
                print("")
                print("1. Ver inventario.")
                print("2. Añadir productos.")
                print("3. Consultar productos.")
                print("4. Actualizar precios.")
                print("5. Eliminar productos.")
                print("6. Calcular el valor total del inventario.")
                print("")
                option=int(input("Escoja una opción para interactuar con el inventario: "))
                print("")
            if option2==2:
                break
        else:
            print("")
            print("Inventario de productos")
            for productName, price in products:
                print(f"Producto: {productName}. Precio: {price}")
                
            print("Qué desea hace a continuación?")
            print("")
            print("1. Ver menú de opciones")    
            print("2. Salir")
            print("")
            option4=int(input(""))
            if option4==1:
                print("")
                print("1. Ver inventario.")
                print("2. Añadir productos.")
                print("3. Consultar productos.")
                print("4. Actualizar precios.")
                print("5. Eliminar productos.")
                print("6. Calcular el valor total del inventario.")
                print("")
                option=int(input("Escoja una opción para interactuar con el inventario: "))
                print("")
            if option4==2:
                break

    if option==2:
        productName=input("Ingrese el nombre del producto: ")
        products["precio"]=float(input(f"Ingrese el precio de {productName}: "))
        products["cantidad"]=int(input(f"Ingrese la cantidad de {productName} disponible: "))
        inventory[productName]=products
        print(f"El producto '{productName}' fue agregado exitosamente.")
        print("")
        print("Qué desea hacer a continuación?")
        print("")
        print("1. Ver el menú de opciones")
        print("2. Agregar un nuevo producto")
        print("3. Salir")
        print("")
        option3=int(input(""))
        if option3==1:
            print("")
            print("1. Ver inventario.")
            print("2. Añadir productos.")
            print("3. Consultar productos.")
            print("4. Actualizar precios.")
            print("5. Eliminar productos.")
            print("6. Calcular el valor total del inventario.")
            print("")
            option=int(input("Escoja una opción para interactuar con el inventario: "))
            print("")
        if option3==2:
            productName=input("Ingrese el nombre del producto: ")
            products["price"]=float(input(f"Ingrese el precio de {productName}: "))
            products["quantity"]=int(input(f"Ingrese la cantidad de {productName} disponible: "))
            print(f"El producto '{productName}' fue agregado exitosamente.")
            print("")
            print("Qué desea hacer a continuación?")
            print("")
            print("1. Ver el menú de opciones")
            print("2. Agregar un nuevo producto")
            print("3. Salir")
            print("")
            option3=int(input(""))
        if option3==3:
            break
        

