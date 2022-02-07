"""
Datos de entrada:
Cantidad de hombres-->C_Homb-->int
Cantidad de mujeres-->C_Mujer-->int
Datos de Salida
Total estudiantes-->T-->int
Porcentaje Hombres-->ph-->float
Porcentaje Mujeres-->pm-->float
"""
#Entrada
C_Homb=int(input("Digite cantidad de hombres: "))
C_Mujer=int(input("Digite cantidad de mujeres: "))
#Caja negra
T=(C_Homb+C_Mujer)
ph=(C_Homb/T)*100
pm=(C_Mujer/T)*100
#Salidas
print("EL porcentaje de hombres es: ",ph,"%")
print("El porcentaje de mujeres es : ",pm,"%")
