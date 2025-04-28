Algoritmo JuegoAleatorio
	Definir num Como Real
	Definir dato Como Real
	num <- Aleatorio(1,10)
	Repetir
		Escribir "Adivina un numero del 1 al 10, Decime un numero"
		Leer dato
		Si dato <> num Entonces
			Si dato > num Entonces
				Escribir "Es muy grande"
			SiNo 
				Escribir "Es muy bajo"
			FinSi
		SiNo
			Escribir "Felicitaciones era ", num
		FinSi
	Hasta Que dato = num
FinAlgoritmo
