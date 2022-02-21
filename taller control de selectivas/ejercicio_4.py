"""
datos de entrada
numero de piezas--->np--->int
costo de las piezas--->cp--->int
"""
#entrada
np=int(input("ingrese la cantidad de piezas: "))
cp=int(input("ingrese el costo de las piezas: " ))
#caja negra
mtc=np*cp
if(mtc>5000000):
    inv=mtc*0.55
    ban=mtc*0.30
    cdf=mtc*0.15
elif (mtc<5000000):
    inv=mtc*0.70
    ban=mtc*0
    cdf=mtc*0.30
itr=cdf*0.20
print("la inversion de los fondos de la empresa: ",inv)
print("la cantidad prestada por el banco es:",ban)
print("la cantidad a pagar a credito es:",cdf)
print("la cantidad de intereses es",itr)        