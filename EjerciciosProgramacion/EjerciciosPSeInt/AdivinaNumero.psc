Algoritmo AdivinaNumero
	Definir ValorAdiv Como Entero
	Definir Ingreso Como Entero
	ValorAdiv = Aleatorio(1,10)
	Mientras ValorAdiv <> Ingreso Hacer
		Escribir 'Este algoritmo, va intentar jugar con vos, decime un numero del 1 al 10'
		Leer Ingreso
		Si ValorAdiv <> Ingreso Entonces
			Escribir 'Intenta Nuevamente'
		FinSi
	FinMientras
Escribir 'Felicitaciones adivinaste'

FinAlgoritmo
