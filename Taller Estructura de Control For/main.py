archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M 
m=0
lista=[]
ciudad_M=[]
for i in archivo:
  a=i.index(":")
  for q in range(a+2, len(i)-1):
    lista.append(i[q])
    a="".join(lista)
  ciudad_M.append(a)
  lista=[]
for i in ciudad_M:
  if(i[0]=="M"):
    m=m+1
print(m)
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
lista=[]
lista2=[]
ciudad_U=[]
pais_U=[]
for i in archivo:
  a=i.index(":")
  for q in range(a+2, len(i)-1):
    lista.append(i[q])
    a="".join(lista)
  ciudad_U.append(a)
  lista=[]
  N=i.index(":")
  for t in range(0, N):
    lista2.append(i[t])
    N="".join(lista2)
  pais_U.append(N)
  lista2=[]
for i in pais_U:
  if(i[0]=="U"):
    print(i) 
for i in ciudad_U:
  if(i[0]=="U"):
    print(i)
#Cuente e imprima cuantos paises que hay en el archivo
lista=[]
contador=0
for i in archivo:
  e=i.index(":")
  for r in range(0,e):
    lista.append(i[r])
  e="".join(lista)
  print(e)
  contador=contador+1
  print(contador)
  lista=[]
for i in archivo:
  e=i.index(":")
  for r in range(0,e):
    lista.append(i[r])
  e="".join(lista)
  print(e)
  lista=[]
#Busque e imprima la ciudad de Singapur
lista=[]
ciudades=[]
for i in archivo:
  A=i.index(":")
  for r in range(A+2,len(i)-1):
    lista.append(i[r])
  A="".join(lista)
  ciudades.append(A)
  lista=[]
for i in ciudades:
  if(i=="Singapur"):
    print(i)
#Busque e imprima el pais de Venezuela y su capital
lista=[]
pais=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  for r in lista:
    pais.append(r)
for i in pais:
  if i=="Venezuela: Caracas\n":
    print(i)
    break
  lista=[] 
#Cuente e imprima las ciudades que su pais inicie con la letra E
lista=[]
paises=[]
ciudad_e=[]
ciudad=[]
for i in archivo:
  lista.append(i)
for i in lista:  
  if(i[0]=="E"):
    ciudad_e.append(i)
  C="".join(ciudad_e)  
for i in ciudad_e:
  A=i.index(":")     
  for r in range(A+2,len(i)-1):
    ciudad.append(i[r])
  B= "".join(ciudad)  
for i in ciudad:
    print(i,end="")
#Buesque e imprima la Capiltal de Colombia
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i=="Bogotá"):
    print(i)
#imprima la posicion del pais de Uganda
c=0 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
#imprima la posicion del pais de Mexico
c=0 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
lista=[]
for i in archivo:
  lista.append(i)
lista.remove("Madagascar: rey julien\n")
lista.insert(109,"Madagascar: Antananarivo\n")
print(lista)
#Agregue un país que no esté en la lista 
lista=[]
for i in archivo:
  lista.append(i)
lista.insert(136,"Palestina: Jerusalem\n")
print(lista)

archivo.close()
