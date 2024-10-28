print("Esta funcion calcula la hipotenusa de un triangulo rectangulo")
## Solicito los valores al usuario
CatetoA = float(input("Dame el valor de A: "))
CatetoB = float(input("Dame el valor de B: "))

while CatetoA <= 0 or CatetoB <=0:
    print("Error, Catetos deben ser mayor que cero")
    CatetoA = float(input("Dame el valor de A: "))
    CatetoB = float(input("Dame el valor de B: "))

if CatetoA > 0: ##OJO CON EL VALOR, debe ser mayor que 0
    if CatetoB > 0:
        print(f"El valor de la hipotenusa es: {(CatetoA**2+CatetoB**2)**1/2}")
    else:
        print("B es menor o igual a Cero, esto es un error")
else:
    print("A es menor o igual a Cero, esto es un error")
