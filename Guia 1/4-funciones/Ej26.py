x = int(input("ingrese el primer nuemro = "))
n = int(input("ingrese el segundo numero = "))

def expo (x,n):
    for i in range(1,n):
     x*=x

    return x

    
print (expo(x,n))
