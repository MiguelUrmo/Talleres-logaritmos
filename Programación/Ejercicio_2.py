"""
Datos de entrada
Dinero invertido-->DI-->int
Datos de salida
Interes mensual-->IM-->int
Dinero ganado-->DG-->int
"""
#Entradas
DI=int(input("Digite cantidad de dinero a invertido: "))
#Caja negra
IM=(DI*0.02)
DG= (DI+IM)
#Salida
print("La cantidad de dinero a final de mes será: ",DG)



