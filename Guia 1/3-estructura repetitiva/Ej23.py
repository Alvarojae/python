pMayor1=0
pMayor2=0
pMayor3=0
c=True

while c:
    a = int(input("ingrese numeros = "))

    if a>pMayor1:
        pMayor3=pMayor2
        pMayor2=pMayor1
        pMayor1=a
        
    elif a>pMayor2:
        pMayor3=pMayor2
        pMayor2=a
    
    elif a>pMayor3:
        pMayor3=a
        

    b = input("ingrese s si quiere parar = ")
    if b == "s":
        c=False
   

print("el numero menor es =",pMayor1)
print("el numero menor es =",pMayor2)
print("el numero menor es =",pMayor3)