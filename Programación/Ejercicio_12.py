"""
datos de entrada
examen--->exm--->float
tarea1--->t1m--->float
tarea2--->t2m--->float
tarea3--->t3m--->float
#fisica
examen--->exf--->float
tarea1--->t1f--->float
tarea2--->t2f--->float
#quimica
examen--->exq--->float
tarea1--->t1q--->float
tarea2--->t2q--->float
tarea3--->t3q--->float
datos de salida
promedios examen--->pexm--->float
promedio traeas--->prtm--->float
#fisica
promedios examen--->pexf--->float
promedio traeas--->prtf--->float
#quimica
promedios examen--->pexq--->float
promedio tareas--->prtq--->float
"""
#entradas
exm=float(input("diigita la nota del examen matematicas: "))
t1m=float(input("digita nota de la tarea 1: "))
t2m=float(input("digita nota de la tarea 2: "))
t3m=float(input("digita nota de la tarea 3: "))
#fisica
exf=float(input("diigita la nota del examen fisica: "))
t1f=float(input("digita nota de la tarea 1: "))
t2f=float(input("digita nota de la tarea 2: "))
#quimica
exq=float(input("diigita la nota del examen quimica: "))
t1q=float(input("digita nota de la tarea 1: "))
t2q=float(input("digita nota de la tarea 2: "))
t3q=float(input("digita nota de la tarea 3: "))
#caja negra
pexm=(exm*0.90)
prtm=(t1m+t2m+t3m)/3*0.10
pexf=(exf*0.80)
prtf=(t1f+t2f)/2*0.20
pexq=(exq*0.85)
prtq=(t1q+t2q+t2q)/3*0.15
#salidas
print("la nota final de matematicas es: ", pexm+prtm)
print("la nota final de fisica es: ", pexf+prtf)
print("la nota final de quimica es: ", pexq+prtq)