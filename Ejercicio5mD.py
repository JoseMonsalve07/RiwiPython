def addStudent():
    name = input("Ingrese su nombre: ")
    grades = []
    for i in range(3):
        grade=float(input(f"Ingrese la nota {i+1} del estudiante: "))
        grades.append(grade)
    return name, grades

def calculateAverage(grades):
    return sum(grades)/3

def results(average):
    if average>=3.0:
        print("El estudiante ha aprobado.")
    else:
        print("El estudiante ha reprobado.")

def main():
    students=int(input("Ingrese la cantidad de estudiantes: "))
    if students > 0:
        for i in range(students):
            print(f"--- Estudiante {i+1} ---")
            name, grades = addStudent()
            average=calculateAverage(grades)
            print(f"El promedio de {name} es: {average:.2f}")
            results(average)
    else:
        students=int(input("Ingrese al menos un estudiante: "))        

main()