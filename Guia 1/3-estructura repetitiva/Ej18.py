menor=100
mayor=0
banderaMa=0
banderaMe=0
i=1
c=True

while c:
    a = int(input("ingrese numeros = "))

    if a<menor:
        menor=a
        banderaMe=i
    if a>mayor:
        mayor=a
        banderaMa=i

    b = input("ingrese s si quiere parar = ")
    if b == "s":
        c=False
    i +=1

print("el numero menor es =",menor,"y fue ingresado en el intento =",banderaMe)
print("el numero mayor es =",mayor,"y fue ingresado en el intento =",banderaMa)