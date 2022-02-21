"""
datos de entrada
distacia recorrida--->dr--->int
"""
#entrada
dr=int(input("ingresar la dstancia recorridaen km: "))
#caja negra
if(dr<=300):
    pag=50000
elif(dr>1000):
    pag=70000+(30000*(dr-300))
elif(dr>1000):
    pag=150000+(9000*(dr-1000)+(30000*(dr-300)))  
#salida
print("el cliente debe pagar: ",pag)      
