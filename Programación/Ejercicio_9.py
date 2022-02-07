"""
Datos de entrada    
Valor de cada Hora trabajada-->VH-->int
Numero de horas trabajadas-->H-->int
Datos de salida
Salario total-->ST-->int
valor del descuento-->VD-->int
Valor salario final-->SF-->int
"""
#entradas
H=int(input("Digite numero de horas trabajadas: "))
VH=int(input("digite valor de cada hora de trabajo: "))
#Caja negra
ST=VH*H
VD=ST*0.2
SF=ST-VD
#salidas
print("el valor final del salario es de]: ",SF)