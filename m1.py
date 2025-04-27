#Se le pregunta al usuario qué producto desea por medio de un input que es guardado en una variable
Product= input("Qué producto deseas? ")

#Se le pregunta al usuario el precio del producto, se hace uso de un condicional para determinar si el precio es el indicado para continuar con la compra
Price= int(input("Qué precio tiene este producto por cada unidad? "))
if Price <= 0:
    print("El precio del producto debe ser mayor a 0")
    Price= int(input("Qué precio tiene este producto por cada unidad? "))
else:
    Price=Price

#Se le pregunta al usuario la cantidad deseada del producto, se hace uso de un condicional para asegurarse que ingrese una cantidad valida para continuar con la compra    
Amount= int(input("Cuántas unidades de este producto deseas? "))
if Amount <= 0:
    print("Debes ordenar una cantidad mayor a 0")
    Amount= int(input("Cuántas unidades de este producto deseas? "))
else:
    Amount=Amount    

#Se le pregunta al usuario si desea agregar un descuento a la compra
Q=input("Desea agregar un descuento a la compra? Responda SI o NO")
if Q == "si":
    Discount= int(input("Ingrese un descuento para el total "))
if Q == "no":
    Discount=0

#En el caso de haber un descuento en la compra, se procede a preguntarle al usuario el porcentaje de descuento deseado
if 0 <= Discount <= 100:
    Discount=Discount 
else:
    Discount=int(input("El porcentaje debe estar en un rango de 0 a 100"))
Total= Price*Amount
TotalWDisc= Total - (Total*Discount/100)

#Se procede a imprimir la factura de compra   
print("Excelente! Compra finalizada.")
print("Producto: " ,(Product))
print("Cantidad: " , (Amount))
print("Precio total: " , (Total))
print("Precio total con descuento: " , (TotalWDisc))