def calculateAverage(grades):
    return sum(grades)/len(grades)

def addStudent():
    name = input("Ingrese su nombre: ")
    grades = []
    for i in range(3):
        grade=float(input(f"Ingrese la nota {i+1} del estudiante: "))
        grades.append(grade)
    return name, grades

def results(average):
    if average>=3.0:
        print("El estudiante ha aprobado.")
    else:
        print("El estudiante ha reprobado.")