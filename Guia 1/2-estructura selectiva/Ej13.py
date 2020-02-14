a = int(input("ingrese cantidad en segundos= "))
dias =     int((a/60/60/24))
horas =    int(((a/60/60%24)*60)/60)
minutos =  int(((a/60/60%24)*60)%60 )
segundos = int(((minutos%60)*60)%60)
print("dias = ",dias,"\nhoras= ",horas,"\nminutos= ", minutos,"\nsegundos= ",segundos)


