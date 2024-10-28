frase = "Tres tristes tigres comen trigo en un trigal"
j = 1 #Contador de palabras
for i in frase:
    if i == " ":
        j +=1

print(f"La cantidad de palabras totales es: {j}")