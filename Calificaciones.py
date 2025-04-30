# 1. Pedir al usuario una calificación numérica que vaya entre 0 y 100
# 2. Determinar si el usuario aprobó o reprobó
# 3. Pedir al usuario una lista de calificaciones del 1 al 100 separadas por comas

# 4. Calcular y mostrar el promedio de las calificaciones en la lista
# 5. Preguntar al usuario por un valor específico
# 6. Contar cuántas calificaciones en la lista son mayores que este valor

grade=float(input("Ingrese una calificación numérica de 0 a 100 "))
while grade < 0 or grade > 100:
    grade=int(input("Ingrese un valor válido. Solo se aceptan valores entre 0 y 100 "))
if grade >= 70:
    print("Usted ha aprobado")
else:
    print("Usted ha reprobado") 

grades=input("Ingrese sus calificaciones separadas por comas ',': ").split(",")
floatGrades= [float(i) for i in grades]
for grade in floatGrades:
    Addition=sum(floatGrades)
    Average=Addition/len(floatGrades)
print(f"El promedio de las calificaciones en la lista es: {Average}")

specificValue=float(input("Ingrese un valor para contar cuántas calificaciones en la lista son mayores que este valor: "))
gradeGreatherThanTheValue=0
noteCounter=0
while noteCounter<len(floatGrades):
    if specificValue<floatGrades[noteCounter]:
        gradeGreatherThanTheValue+=1
    noteCounter+=1 
print(f"Total de calificaciones mayores al valor indicado: {gradeGreatherThanTheValue}")

specificGrade=float(input("Ingrese una nota para verificar si está en sus notas y contar cuántas veces está: "))
repeatedGradeCounter=0
for isTheGrade in floatGrades:
    if specificGrade==isTheGrade:
        repeatedGradeCounter+=1
    else:
        continue    
print(f"Total de calificaciones con este mismo valor: {repeatedGradeCounter}")
