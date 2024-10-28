## Funciones definidas para la calculadora
def suma(x,y):
    return print(x+y)
def resta(x,y):
    return print(x-y)
def mult(x,y):
    rmult = x*y
    return print(rmult)
def div(x,y):
    return print(x/y)
def poten(x,y):
    return print(x**y)
def raiz(x,y=2):
    return print(x**(1/y))

## Funcion Calculadora:
a = float(input("Dame el valor A "))
b = float(input("Dame el valor B "))
print("A - Sumar, B - Resta, C - Multiplicacion, D - Division")
oper = str(input("Selecciona la opcion deseada "))

match oper:
    case "A":
        suma(a,b)
    case "B":
        resta(a,b)
    case "C":
        mult(a,b)
    case "D":
        div(a,b)
    case "E":
        poten(a,b)
    case "F":
        raiz(a,b)