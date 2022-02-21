"""
datos de entrada
variable 1--->a--->int
variable 2--->b--->int
variable 3--->c--->int
variable 4--->d--->int
"""
#entrada
a=int(input("ingrese variable 1: " ))
b=int(input("ingrese variable 2: "))
c=int(input("ingrese variable 3: "))
d=int(input("ingrese variable 4: "))
#caja negra
if (d==0):
    re=(a-c)**2
elif(d>0):
    re=((a-b)**3)/d
    print("el valor es: ",re)    

