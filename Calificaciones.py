# Jose Manuel Bustamante Monsalve

# 1. Pedir al usuario una calificación numérica que vaya entre 0 y 100
# 2. Determinar si el usuario aprobó o reprobó
# 3. Pedir al usuario una lista de calificaciones del 1 al 100 separadas por comas
# 4. Calcular y mostrar el promedio de las calificaciones en la lista
# 5. Preguntar al usuario por un valor específico
# 6. Contar cuántas calificaciones en la lista son mayores que este valor
 
# Se le pide al usuario que ingrese la nota mínima para ganar, asegurandonos de que ingrese un numero válido.
gradeToWin=float(input("Ingrese la nota mínima para ganar (Valores entre 0 y 100): "))
while gradeToWin < 0 or gradeToWin > 100:
    gradeToWin=float(input("Ingrese un valor válido. Solo se aceptan valores entre 0 y 100: "))

# Se le pide al usuario una calificación, se le va a indicar si aprobó o reprobó, y se le advierte que esta será agregada a la lista que ingresará a continuación.
grade=float(input("Ingrese una calificación numérica de 0 a 100 (Esta se agregará a las siguientes calificaciones): "))
while grade < 0 or grade > 100:
    grade=float(input("Ingrese un valor válido. Solo se aceptan valores entre 0 y 100: "))
if grade >= gradeToWin:
    print("Usted ha aprobado")
else:
    print("Usted ha reprobado") 

# El usuario ingresa la lista de calificaciones separadas por comas, las calificaciones se convierten en tipo float usando un ciclo for
# y luego se agrega a la lista la calificación ingresada previamente. (https://www.freecodecamp.org/espanol/news/python-lista-append-como-agregar-elementos-a-una-lista-explicado-con-ejemplos/) 
# Se hace uso de un ciclo for para determinar si aprobó o reprobó su promedio.
grades=input("Ingrese sus calificaciones separadas por comas ',': ").split(",")
floatGrades= [float(i) for i in grades]
floatGrades.append(grade)
for grade in floatGrades:
    Addition=sum(floatGrades)
    Average=Addition/len(floatGrades)
if Average>gradeToWin:
        print(f"Según la nota mínima que usted ingresó para ganar ({gradeToWin}), usted ha aprobado su promedio")
if Average<gradeToWin:
        print(f"Según la nota mínima que usted ingresó para ganar ({gradeToWin}), usted ha reprobado su promedio")    
print(f"Las calificaciones ingresadas fueron {floatGrades}. El promedio de las calificaciones en la lista es: {Average}")

# Se le indica al usuario que ingrese un valor, esto para compararlo con las notas ingresadas en la lista e indicarle cuantas notas
# son mayores que el valor ingresado.
specificValue=float(input("Ingrese una nota para contar cuántas en la lista son mayores que esta: "))
gradeGreatherThanTheValue=0
noteCounter=0
while noteCounter<len(floatGrades):
    if specificValue<floatGrades[noteCounter]:
        gradeGreatherThanTheValue+=1
    noteCounter+=1 
print(f"Total de calificaciones mayores al valor indicado: {gradeGreatherThanTheValue}")

# Se le pide al usuario que ingrese otra nota 
specificGrade=float(input("Ingrese una nota para verificar si está en sus notas y contar cuántas veces está: "))
repeatedGradeCounter=0
for isTheGrade in floatGrades:
    if specificGrade==isTheGrade:
        repeatedGradeCounter+=1
    else:
        continue    
print(f"Total de calificaciones con este mismo valor: {repeatedGradeCounter}")
