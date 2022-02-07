"""
Datos de entrada:
Lado a-->A-->int
lado b-->B-->int
lado c-->C-->int
Datos de salida
semiperimetro-->s-->int
area-->Ar-->int
"""
#Entradas
from cmath import sqrt
A=int(input("Digite valor lado A: "))
B=int(input("Digite valor lado B: "))
C=int(input("Digite valor lado C: "))
#caja negra
s=(A+B+C)/2
Ar=sqrt(s(s-A)*(s-B)*(s-C))
#Salida
print("El valor de la raiz es: ",Ar)
print("El valor del semiperimetro es: ",s)
