Algoritmo LogiSemaforo
	Definir semaforo Como Caracter
	// Falta asignar contador
	Definir contador Como Entero
	contador = 0
	semaforo <- "Verde"
	Escribir semaforo
	Repetir
		Si semaforo = "Verde" Entonces
		semaforo <- "Amarillo"
		esperar 5 Segundos
		Escribir semaforo
			si semaforo = "Amarillo" Entonces
				semaforo <- "Rojo"
				Esperar 3 segundos
				Escribir semaforo
				si semaforo = "Rojo" Entonces
					semaforo <- "Verde"
					Esperar  5 Segundos
					Escribir semaforo
					// Agregar incremento a contador
					contador = contador + 1
				FinSi
			FinSi
		FinSi
	Hasta Que contador = 3
FinAlgoritmo
