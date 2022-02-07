"""
Datos de Entrada
Sueldo Base-->SB-->int
Valor venta uno-->VU-->int
Valor venta dos-->VD-->int
Valor ventra tres-->VT-->int
Datos de salida
Valor Comisión por venta 1-->VC1-->int
Valor Comisión por venta 2-->VC2-->int
Valor Comisión por venta 3-->VC3-->int
Sueldo neto final-->SF-->int
"""
#Entradas
SB=int(input("Digite sueldo base: "))
VU=int(input("Digite valor venta uno: "))
VD=int(input("Digite valor venta dos: "))
VT=int(input("Digite valor venta tres: "))
#Caja negra
VC1=VU*0.1
VC2=VD*0.1
VC3=VT*0.1
SF=SB+VC1+VC2+VC3
#Salidas
print("Su sueldo final será de: ",SF, "COP")