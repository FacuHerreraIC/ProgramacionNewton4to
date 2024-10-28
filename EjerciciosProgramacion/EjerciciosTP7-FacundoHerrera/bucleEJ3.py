PIN_SECRETO = "1234"
i = 3
while i > 0:
    INGRESO = str(input("Ingrese la contraseña: "))
    if PIN_SECRETO == INGRESO:
        print("Bienvenido a su sistema")
        break
    elif i < 0 :
        print("Llamando a la policia")
        break
    else:
        i -= 1
        print(f"Error, intente nuevamente, restan {i} intentos")