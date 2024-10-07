#Parte 1 - Sin pedir datos
#Ci = 100000
#i = 0.02
#n = 10

#Parte 2 - Pedir datos
Ci = int(input('Ingresar el valor del capital inicial: '))
i = float(input('Indicar el valor de interes (En decimales): '))
n = int(input('Indicar cantidad de ciclos/años: '))
Cf = Ci *(1 + i)**n
print(f"El Valor final, con un capital de {Ci}, un interes de {i} con la cantidad de años {n} es ")
print(Cf)