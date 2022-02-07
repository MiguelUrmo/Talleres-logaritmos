"""
Datos de entrada
Promedio de notas parciales-->PN-->int
Calificación examen final-->EF-->int
Calificacion trabajo final-->TF-->int
Datos de salida
Valor final nota parciales-->VP-->float
Valor final examen final-->VE-->float
Valor final trabajo final-->VT-->float
Nota final-->NF-->float
"""
#Entradas
PN=int(input("Digite promedio notas parciales: "))
EF=int(input("Digite nota examen final: "))
TF=int(input("Digite nota trabajo final: "))
#Caja negra
VP=PN*0.55
VE=EF*0.3
VT=TF*0.15
NF=VP+VE+VT
#Salida
print("Su nota final es de: ",NF)