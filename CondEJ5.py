seleccion = str(input("Bienvenido a Bella Napoli, ¿Quiere una pizza vegetariana? SI/NO"))
if seleccion == "SI":
    ingrediente = str(input("Selecciono Vegetariano, elija su ingrediente; Tofu o Pimiento"))
    if ingrediente == "Pimiento":
        print("Usted eligio Vegetariano con Pimiento")
    else:
        print("Usted eligio Vegetariano con Tofu")
else:
    ingrediente = str(input("Selecciono No Vegetariano, elija su ingrediente; Peperoni, Jamon o Salmon"))
    if ingrediente == "Peperoni":
        print(f"Usted eligio No Vegetariano con {ingrediente}")
    elif ingrediente == "Jamon":
        print(f"Usted eligio No Vegetariano con {ingrediente}")
    else:
        print(f"Usted eligio No Vegetariano con {ingrediente}")
        