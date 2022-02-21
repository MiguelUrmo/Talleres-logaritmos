"""
datos de salida
valor_1--->p--->int
valor_2--->q--->int
"""
p=int(input("ingrese el valor de p: "))
q=int(input("ingrese el valor de q: "))
#caja negra
respuesta=""
e=(p**3+q**4-2*(p**2))
if(e>680):
    print("p y q satisfacen la expresion ")
else:
    print("py q no satisfacen la expresion")
        