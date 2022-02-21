listaa=[]
listanom=[]
listac=[]
estudiantes=int(input("Ingrese el numero de estudiantes: "))
est=int(input("Ingrese 1 para agregar nombres y puntajes: "))
for i in range(0, estudiantes):
    est=input()
    if(est==1):
        Z=(nombre, notafinal)=est.split(" ")
        nombre=str(nombre)
        notafinal=int(notafinal)
        listanom.append(nombre)
        listaa.append(notafinal)
        listac.append(Z)
        mediaN=sum(listaa)/len(listaa)
        n = [i for i in listaa if i>mediaN]       
        inf=(len(n)*100)/len(listaa)
        Z = [i for i in listaa if i<mediaN]
        sup=(len(Z)*100)/len(listaa)
    elif(est>=2):
        break
print("El estudiante con el puntaje más alto es: ", (listac[listaa.index(max(listaa))]))
print("El estudiante con el puntaje más bajo es: ", (listac[listaa.index(min(listaa))]))
print("El puntaje maximo es: ", max(listaa))
print("El puntaje maximo es: ", min(listaa))
print("Media de puntajes: ", mediaN)
print("Porcentaje de estudiantes que estan bajo el promedio: ",inf,"%")
print("Porcentaje de estudiantes que estan sobre el promedio: ",sup,"%")