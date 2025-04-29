#Para poder saber el promedio de hot dogs por concurso
cant_cada_uno=input("Introduzca los valores separados: ") #Entrada se un solo renglon
cant_indiv=cant_cada_uno.split() #Separar las cantidades en dos variables diferentes

#Debemos poner las condiciones dadas por el problema, entonces:
try:
   total_perritos= int(cant_indiv[0]) #Indico la posición
   total_personas= int(cant_indiv[1]) #indica el # de personas
   while True:
      if total_perritos<1:
         print("Inserte un número de perros mayor a 1")
         cant_cada_uno=input("Introduzca los valores separados: ") #Entrada se un solo renglon
         cant_indiv=cant_cada_uno.split()
         total_perritos= int(cant_indiv[0]) #Indico la posición
         total_personas= int(cant_indiv[1]) #indica el # de personas
      elif not(1<=total_personas<=1000):
         print("El número de participantes debe estar entre 1 y 1000")
         cant_cada_uno=input("Introduzca los valores separados: ") #Entrada se un solo renglon
         cant_indiv=cant_cada_uno.split()
         total_perritos= int(cant_indiv[0]) #Indico la posición
         total_personas= int(cant_indiv[1]) #indica el # de personas
      else:
         promedio_perritos= total_perritos/total_personas
          #para LIMITAR decimales
         Total_final="{:.2f}".format(promedio_perritos)
         print("El número promedio de perritos por personas es de: " + str(promedio_perritos))

         break
  
except ValueError:
   print("Error, prueba con dos enteros separados por un espacio") #Para los casos de error
except IndexError:
   print("Error, mejor ingresa dos números separados ")
except ZeroDivisionError:
   print("No pueden haber 0 participantes")




