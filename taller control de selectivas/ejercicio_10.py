"""
datos de entrada
sueldo--->s--->int
categoria--->cat--->int
"""
#entrada
cat=int(input("ingrese la categoria: "))
#caja negra
cat1=(5000000*0.10)+5000000
cat2=(4300000*0.15)+4300000
cat3=(3600000*0.20)+3600000
cat4=(2000000*0.40)+2000000
cat5=(900000*0.60)+900000
if cat==1:
    nsb=cat1
    print("la categoria es: ",cat)
    print("el nuevo sueldo bruto es: ",nsb)
if cat==2:
    nsb=cat2
    print("la categoria es: ",cat)
    print("el nuevo sueldo bruto es: ",nsb)
if cat==3:
    nsb=cat3
    print("la categoria es: ",cat)
    print("el nuevo sueldo bruto es: ",nsb) 
if cat==4:
    nsb=cat4
    print("la categoria es: ",cat)
    print("el nuevo sueldo bruto es: ",nsb)
if cat==5:
    nsb=cat5
    print("la categoria es: ",cat)
    print("el nuevo sueldo bruto es: ",nsb)           