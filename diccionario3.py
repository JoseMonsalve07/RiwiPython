users=[{
    "cc": "123",
    "nombre": "Jose Manuel",
    "apellido": "Bustamante",
    "edad": 17,
    "telefono": "3014349376"
},
{
    "cc": "12",
    "nombre": "Jose",
    "apellido": "Monsalve",
    "edad": 18,
    "telefono": "3015649376"
},
{
    "cc": "345",
    "nombre": "Manuel",
    "apellido": "Bustamante",
    "edad": 23,
    "telefono": "3004549376"
}
]
newUser={
    "cc": "678",
    "nombre": "Joselo",
    "apellido": "Bustamante",
    "edad": 15,
    "telefono": "3014349376"
}

users.append(newUser)

for user in users:
    if user["cc"]=="345":
        print(f"Datos: Nombre: {user["nombre"]}, CC: {user["cc"]}")
        break

for user in users:
    if user["cc"]=="678":
        user["edad"]=35
        print(user["edad"])
        break
    
#print(users)
#print(len(users))