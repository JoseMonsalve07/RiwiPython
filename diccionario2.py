information = {
    "nombre": "Jose Manuel",
    "apellido": "Bustamante",
    "edad": 17,
    "telefono": "3014349376"
}

# cambiar datos
information["edad"]=20

# agregar datos
information["cc"]="1035854944"
information["apellido"] = ""
del information["telefono"]

lastName=input("Ingrese su apellido ")
information["apellido"]=lastName
print(information)
