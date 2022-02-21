"""
datos de entrada
sueldo base--->sb--->int
"""
#entrada
sb=int(input("ingrese el sueldo base: "))
#caja negra
sa=((sb*0.15)+sb)
sb=((sb*0.12)+sb)
if (sb<900000):
    print("el sueldo total es: ",sa)
else:
    print("el sueldo total es: ",sa)

