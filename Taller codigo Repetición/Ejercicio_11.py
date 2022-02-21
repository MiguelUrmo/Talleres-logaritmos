bebe=int(input("¿Usted bebe licor?, si lo hace digite 1, si no lo hace digite 2: "))
agr=0
ron=0
cerv=0
teq=0
whi=0
otro=0
Bebida=0
listaco=[]
listaco.append(bebe)
listalicor=[]
listaedad=[]
listacer=[]
listawhis=[]
listaHo=[]
listaMu=[]
listat=[]
while True:
    if((bebe==2)):
        print(f"Aguardiente {agr}\nRon {ron}\nCerveza {cerv}\nTequila {teq}\nwhisky {whi}\nOtro {otro}")
        print(len(listaco))
        print(len(listaMu))
        print(sum(listaHo))
        print(len(listawhis)/len(listaco))
        break
    elif(bebe==1):
        edad=int(input("Digite su edad: "))
        listaedad.append(edad)
        sexo=str(input("Ingrese su sexo, digite 1 para sexo femenino y 2 para sexo masculino: "))
        Bebida=int(input("1.Aguardiente, 2.Ron, 3.Cerveza, 4.Tequila, 5.Whisky, 6.Otro: "))
        listalicor.append(Bebida)
        break