mayor=0
menor=100
cantidadMa=1
cantidadMe=1

a = int(input("ingrese la cantidad de numeros = "))
for i in range(a):
    b = int(input("ingrese la cantidad de numeros = "))
    
         
    if b<=menor:
        if b==menor:
            cantidadMe+=1
        menor=b
            
    if b>=mayor:
        if b==mayor:
           cantidadMa+=1
        mayor=b

print("el numero menor es =",menor,"y fue ingresado =",cantidadMe,"veces")
print("el numero mayor es =",mayor,"y fue ingresado =",cantidadMa,"veces")
    
