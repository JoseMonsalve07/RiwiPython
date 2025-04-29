# 1. Pedir al usuario una calificación numérica que vaya entre 0 y 100
# 2. Determinar si el usuario aprobó o reprobó
# 3. Pedir al usuario una lista de calificaciones del 1 al 100 separadas por comas

# 4. Calcular y mostrar el promedio de las calificaciones en la lista
# 5. Preguntar al usuario por un valor específico
# 6. Contar cuántas calificaciones en la lista son mayores que este valor

Grade1=int(input("Ingrese una calificación numérica de 0 a 100 "))
while Grade1 < 0 or Grade1 > 100:
    Grade1=int(input("Ingrese un valor válido. Solo se aceptan valores entre 0 y 100 "))
if Grade1 >= 60:
    print("Usted ha aprobado")
else:
    print("Usted ha reprobado") 

Grades=input("Ingrese sus calificaciones separadas por comas ',': ").split(",")
FloatGrades= [float(x) for x in Grades]
sum=0

for grade in FloatGrades:
    sum += grade
    avg=sum/len(FloatGrades)
print(f"El promedio de las calificaciones en la lista es: {avg}")

specificValue=float(input("Ingrese un valor para contar cuántas calificaciones en la lista son mayores que este valor"))


print(grade)
print(FloatGrades)
print(Grades)