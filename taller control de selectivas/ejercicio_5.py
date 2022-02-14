"""
datos de entrada
sueldo--->s--->int
ventas realizadas departamento 1--->vrd1--->int
ventas realizadas departamento 2--->vrd2--->int
ventas realizadas departamento 3--->vrd3--->int
"""
#entradas
s=int(input("ingrese el sueldo base: "))
vrd1=int(input("ingrese el numero de ventas realizadas por departamento 1: "))
vrd2=int(input("ingrese el numero de ventas realizadas por departamento 2: "))
vrd3=int(input("ingrese el numero de ventas realizadas por departamento 3: "))
#caja negra
vt=(vrd1+vrd2+vrd3)
por=(vt*33/100)
if(vrd1>por):
    s1=s+s*0.20
    print("ventas mayor al 33%",s1)
else:
    print("venta menor al 33%",s)
if (vrd2>por):
    s2=s+s*0.20
    print("ventas mayor al 33%",s2)
else:
    print("venta menor al 33%",s)
if (vrd3>por):
    s3=s+s*0.20
    print("venta mayor a 33%",s3)
else:
    print("venta menor al 33%",s)        
