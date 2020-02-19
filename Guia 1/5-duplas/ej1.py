a = int(input("ingrese un numero= "))
def encontrarPrimos(a):
    vector=[""]*a
    aux=0

    for j in range(2,a):
        bandera=0
        for i in range(2,a):
            if j%i==0:
                bandera+=1
        if bandera==1: 
            vector[aux]=j
            aux+=1
    print (vector[0:aux])

encontrarPrimos(a)

input()