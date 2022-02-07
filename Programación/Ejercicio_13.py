"""
Datos de entrada
billestes de 50k-->cin-->int
billetes de 20k-->vei-->int
billetes de 10k-->die-->int
billetes de 5k-->cin-->int
billetes de 2k-->dos-->int
billetes de 1k-->uno-->int
billetes de 500-->qui-->int
billetes de 100-->cie-->int
Datos de salida
Total de 50k-->Tc-->int
Total de 20k-->Tv-->int
Total de 10k-->Td-->int
Total de 5k-->Tci-->int
Total de 2k-->Tdo-->int
Total de 1k-->Tu-->int
Total de 500-->Tq-->int
Total de 100-->Tcie-->int
Cantidad de dinero-->T-->int
"""
#entradas
cin=int(input("Digite cantidad billetes de 50k: "))
vei=int(input("digite cantidad billetes de 20k: "))
die=int(input("digite cantidad billetes de 10k: "))
cin=int(input("digite cantidad billetes de 5k: "))
dos=int(input("digite cantidad billetes de 2k: "))
uno=int(input("Digite cantidad billetes de 1k: "))
qui=int(input("Digite cantidad billetes de 500: "))
cie=int(input("Digite cantidad billetes de 100: "))
#caja negra
Tc=cin*50000
Tv=vei*20000
Td=die*10000
Tci=cin*5000
Tdo=dos*2000
Tu=uno*1000
Tq=qui*500
Tcie=cie*100
T=Tc+Tv+Td+Tci+Tdo+Tu+Tq+Tcie
#salida
print("La cantidad total de dinero es de: ",T," COP")