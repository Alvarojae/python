import math
base = int(input("ingrese la base = "))
altura = int(input("ingrese la altura = "))
ladoFaltante=math.sqrt(base**2+altura**2)
perimetro = base+altura+ladoFaltante
superficie = (base*altura)/2
print("el perimetro es = ",perimetro)
print("la superficie es = ",superficie)