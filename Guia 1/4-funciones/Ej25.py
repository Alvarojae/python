from math import sqrt
A=int(input("ingrese el primer valor = "))
B=int(input("ingrese el segundo valor = "))
C=int(input("ingrese el tercer valor = "))

def cuadratica(A,B,C):
    resultado=False

    if sqrt((B**2-(4*A*C))) > 0:

        x1 = (-B+sqrt((B**2-(4*A*C)))/(2*A))
        x2 = (-B-sqrt((B**2-(4*A*C)))/(2*A))
        print("primer raiz  = ",x1)
        print("segunda raiz = ",x2)
        resultado = True
    return resultado

if cuadratica(A,B,C) == True:
    print(cuadratica(A,B,C))
else:
    print("no tiene raices")