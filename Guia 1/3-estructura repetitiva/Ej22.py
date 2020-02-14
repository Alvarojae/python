bandera=0
a = int(input("ingrese un numero para saber si es primo= "))
for i in range(2,11):
    if a%i==0:
        bandera+=1
if bandera>1:
    print(a,"no es un numero primo")
else:
    print(a,"es un numero primo")