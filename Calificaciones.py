# Jose Manuel Bustamante Monsalve

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

# Se le indica al usuario que ingrese una nota, esto para compararla con las ya ingresadas en la lista e indicarle cuantas
# son mayores que el valor ingresado.
specificValue=float(input("Ingrese una nota para contar cuántas en la lista son mayores que esta: "))
gradeGreatherThanTheValue=0
noteCounter=0
while noteCounter<len(floatGrades):
    if specificValue<floatGrades[noteCounter]:
        gradeGreatherThanTheValue+=1
    noteCounter+=1 
print(f"Total de notas mayores al valor indicado: {gradeGreatherThanTheValue}")

# Se le pide al usuario que ingrese otra nota, esto para verificar cuántas veces se repite esta dentro de la lista e indicarle al usuario.
specificGrade=float(input("Ingrese una nota para verificar si está en sus notas y contar cuántas veces está: "))
repeatedGradeCounter=0
for isTheGrade in floatGrades:
    if specificGrade==isTheGrade:
        repeatedGradeCounter+=1
    else:
        continue    
print(f"Total de calificaciones con este mismo valor: {repeatedGradeCounter}")

# BIBLIOGRAFÍA
# https://www.freecodecamp.org/espanol/news/python-lista-append-como-agregar-elementos-a-una-lista-explicado-con-ejemplos/
# SE USÓ PARA ENCONTRAR EL USO DEL MÉTODO: floatGrades.append(grade)