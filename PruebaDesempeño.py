# Prueba de desempeño - Módulo 1
# Fundamentos de programación con Python
# JOSE MANUEL BUSTAMANTE MONSALVE

inventory = []

# Displays the options menu for interacting with the inventory
def menu():
    print("\n--- BIENVENIDO ---\n")
    print("1. Ver inventario.")
    print("2. Añadir productos.")
    print("3. Consultar productos.")
    print("4. Actualizar precios.")
    print("5. Eliminar productos.")
    print("6. Calcular el valor total del inventario.")
    print("7. Salir.\n")

menu() # Print the options menu
option=int(input("Escoja una opción para interactuar con el inventario: "))

def emptyInventory():
        # This function prints a message indicating that the inventory is empty.
        print("\nEl inventario está vacío.\n")

def seeInventory():
    #Esta función muestra la lista de productos en el inventario, incluyendo su nombre, precio y cantidad.
    i=0 # Se inicia un contador para enumerar los productos.
    print("Los productos en el inventario son los siguientes: \n")
    for product in inventory: # Se itera sobre cada producto en la lista inventory.
        i+=1 # Se incrementa el contador por cada producto que itere.
        print(f"Producto #{i}:\n Nombre: {product["Nombre"]}\n Precio: {product["Precio"]}\n Cantidad: {product["Cantidad"]}\n")

seeInventory()
