# 1. Pedir al usuario una calificación numérica que vaya entre 0 y 100
# 2. Determinar si el usuario aprobó o reprobó
# 3. Pedir al usuario una lista de calificaciones del 1 al 100 separadas por comas

# 4. Calcular y mostrar el promedio de las calificaciones en la lista
# 5. Preguntar al usuario por un valor específico
# 6. Contar cuántas calificaciones en la lista son mayores que este valor

grade=float(input("Ingrese una calificación numérica de 0 a 100 "))
while grade < 0 or grade > 100:
    grade=int(input("Ingrese un valor válido. Solo se aceptan valores entre 0 y 100 "))
if grade >= 60:
    print("Usted ha aprobado")
else:
    print("Usted ha reprobado") 

grades=input("Ingrese sus calificaciones separadas por comas ',': ").split(",")
floatGrades= [float(i) for i in grades]

for grade in floatGrades:
    add=sum(floatGrades)
    avg=add/len(floatGrades)
print(f"El promedio de las calificaciones en la lista es: {avg}")

specificValue=float(input("Ingrese un valor para contar cuántas calificaciones en la lista son mayores que este valor: "))
for comparedGrade in floatGrades:  
    x=0
    while specificValue==comparedGrade:
        x+=1

print(f"aaa{x}")

print(grade)
print(floatGrades)
print(grades)