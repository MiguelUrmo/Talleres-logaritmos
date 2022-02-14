"""
datos de entrada
deporte--->d--->str
"""
#entrada
t=float(input("ingrese la tempratura "))
#caja negra
deporte=""
if(t>85):
    deporte="natacion"
elif(t>70 and t<=85):
    deporte="tenis"
elif(t>32 and t<=70):
    deporte="golf"
elif(t>10 and t<=32):
    deporte="esqui"
elif(t>=0 and t<=10):
    deporte="marcha"
else:
    deporte="no se encuentra el rango"
#datos de salida
print("el deporte es: "+deporte)            
