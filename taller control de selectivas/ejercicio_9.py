"""
datos de entrada
monto de la compra--->mc--->int
nombre de la compra--->nc--->str
"""
#entrada
nc=str(input("ingrese su nombre: "))
mc=int(input("ingrese el monto de la compra: "))
#caja negra
if(mc<50000):
    print("no hay descuento")
elif(mc>=50000 and mc<100000):
    mp=mc-(mc*0.5) 
    print("cliente: ",nc)
    print("monto de la compra: ",mc)  
    print("el monto a pagar es: ",mp) 
    print("descuento recibido: ",mc*0.5)
elif(mc>=100000 and mc<700000):
    mp=mc-(mc*0.11)
    print("cliente: ",nc)
    print("monto de la compra: ",mc)  
    print("el monto a pagar es: ",mp) 
    print("descuento recibido: ",mc*0.11)
elif(mc>=700000 and mc<1500000):
    mp=mc-(mc*0.18)
    print("cliente: ",nc)
    print("monto de la compra: ",mc)  
    print("el monto a pagar es: ",mp) 
    print("descuento recibido: ",mc*0.18)
elif(mc>=1500000):
    mp=mc-(mc*0.25)
    print("cliente: ",nc)   
    print("monto de la compra: ",mc)  
    print("el monto a pagar es: ",mp) 
    print("descuento recibido: ",mc*0.25)