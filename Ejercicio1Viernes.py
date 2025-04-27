texto=str(input("ingrese un texto "))
max_long= 10
x=len(texto)
if x > max_long:
        texto=len(texto) - max_long
        print(f"{texto} ...")
else:
        print(texto)