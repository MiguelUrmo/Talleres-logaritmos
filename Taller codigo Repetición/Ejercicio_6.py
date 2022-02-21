"""
Dividendo-->D-->int
Divisor-->di-->int
resto-->r-->int
"""
contador=int(0)
D=int(input("Ingrese dividendo: "))
di=int(input("ingrese divisor: "))
D=D-di
r=D%di
while(D>=0):
    contador=contador+1
    D=D-di
print("La division es igual a: ",contador)    
print("El resto es igual a: ",r)
