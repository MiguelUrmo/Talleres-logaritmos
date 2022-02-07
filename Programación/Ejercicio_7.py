"""
Datos de entrada
Numero de Metros-->M-->int
Datos de salida
Numero de Pulgadas-->P-->float
Numero de Pies-->ft-->float
"""
#Entrada
M=int(input("Inserte número de metros a convertir: "))
#Caja negra
P=M*39.27
ft=P/12
#Salida
print("La cantidad de pulgadas es: ",P)
print ("La cantidad de pies es de: ",ft)
