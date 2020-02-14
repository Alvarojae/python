a = int(input("ingrese el primer numero= "))
b = int(input("ingrese el segundo numero= "))

print("\n1-suma\n2-resta\n3-multiplicacion\n4-division\n")

opcion=int(input("ingrese la opcion= "))

if opcion == 1:
    print("la suma es= ",a+b)

elif opcion == 2:
    print("la resta es= ",a-b)

elif opcion == 3:
    print("la multiplicacion es= ",a*b)

elif opcion == 4:
    print("la division es= ",a/b)

else:
    print("ingresaste cualquier numero")
