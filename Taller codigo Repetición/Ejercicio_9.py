A=0
D=0
G=0
while True:
    numero=int(input())
    if(numero==1):
        A=A+1
    elif(numero==2):
        D=D+1
    elif(numero==3):
        G=G+1
    elif(numero==4):     
        break
    print(f"muito obrigado\nAlcool:{A}\nGasolina:{G}\nDiesel:{D}")
else:
    print("inserte numero valido")
