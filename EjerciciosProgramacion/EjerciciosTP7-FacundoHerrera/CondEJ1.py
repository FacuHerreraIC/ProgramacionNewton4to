edad = int(input("Decime tu edad y te digo si podes pasar: "))
acompañado = str(input('Indica si esta acompañado con si o no: '))
if edad >= 18:
    print('podes pasar')
else:
    if acompañado == "si":
        print('Podes pasar')
    else:
        print('No podes pasar')