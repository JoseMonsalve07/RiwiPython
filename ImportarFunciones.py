from Ejercicio5mD import addStudent, calculateAverage, results

#para importar desde otra carpeta
# from "carpeta"."archivo" import "lo que se va a importar"


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