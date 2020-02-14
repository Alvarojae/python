nombreMayor=""
nombreMenor=""
menor=99999
mayor=0
c=True

while c:
    nombre = input("ingrese nombre = ")
    salario = int(input("ingrese salario = "))

    if salario<menor:
        menor=salario
        nombreMenor=nombre
    if salario>mayor:
        mayor=salario
        nombreMayor=nombre

    b = input("ingrese s si quiere parar = ")
    if b == "s":
        c=False


print("el salario mas bajo es  =",menor,"y el nombre es =",nombreMenor)
print("el salario mas alto es =",mayor,"y el nombre es =",nombreMayor)