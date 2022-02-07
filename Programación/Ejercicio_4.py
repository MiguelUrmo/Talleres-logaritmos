"""
Datos de Entrada
Valor Base de compra-->VB-->int
Datos de salida
Valor Descuento-->VD-->int
Valor final de compra-->VF-->int
"""
#Entrada
VB=int(input("Digite valor base de compra: "))
#Caja Negra
VD=VB*0.15
VF=VB-VD
#Salidas
print("El valor final de su compra es de: ",VF, "COP")
