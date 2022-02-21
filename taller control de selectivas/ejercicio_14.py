"""
datos de entrada
lectura actual--->lact--->int
lectura anterior--->lant-->int
datos de salida
monto a pagar-->mp-->float
"""
#entrada
lact=int(input("ingrese la lectura actual: "))
lant=int(input("ingrese la lectura anterior: "))
#caja negra
dif=lant-lact
if(dif>=0) and (dif<=100):
    mpag=dif*4600
elif(dif>=101) and (dif<=300):
    mpag=dif*8000
elif(dif>=301) and (dif<=500):
    mpag=dif*100000
elif(dif>=501):
    mpag=dif*120000
#datos de salida
print("el monto a pagar del suscriptor sera: ",mpag)        
