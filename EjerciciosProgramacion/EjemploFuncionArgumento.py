#Defino la funcion
def mult2(a,b=2):
    return print(a*b)
#Ejecuto el Codigo
x = float(input("Dame el valor a y te lo multiplico por 2"))
y = float(input("Si queres, puedo multiplicarlo por otro valor: "))
#Llamo a la funcion mult2
mult2(x,y)