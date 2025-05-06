print("Bienvenido!")
numberOfUsers=int(input("Cantidad de usuarios a ingresar: "))

def nameAndGrades():
    name=input("Nombre del usuario: ")
    userGrades=input("Ingrese tres notas (Rango de 0 a 5), separadas por comas: ").split(",")
    grades=[float(i) for i in userGrades]
    return name, grades
    
def average(grades):
    return sum(grades)/3

def results(name, averages):
    print(f"Estudiante {name}, su promedio es {averages}")
    if averages>=3.0:
        print("Usted aprobó")
    else:
        print("Usted reprobó")

usersCount=0
for users in range(numberOfUsers):
    while usersCount<numberOfUsers:
        usersCount+=1
        name, grades=nameAndGrades()
        averages=average(grades)
        results(name, averages)
        