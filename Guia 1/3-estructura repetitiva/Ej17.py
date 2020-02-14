b=0
while True:
    a = int(input("ingrese numeros (al poner cero se termina el programa)= "))
    if a==0:
        break
    else:
        b = a+b
        print(b)

print("la sumatoria final de los numero ingresados es = ",b)
    