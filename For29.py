flag = "si"
i=0
while flag != "no":
    print("hola mundo")
    i+=1
    print (f"el mensaje se ha visto {i} vez")
    flag = input("quieres imprimir el mensaje otra vez?")
if flag == "no":
    print(f"el mensaje se repitió {i} veces")
    print("fin del mensaje")    