Algoritmo ContadorHastaN
	Definir n, suma, i Como Entero
	Escribir 'Ingresa un numero positivo'
	Leer n 

	Si n > 0 Entonces
		suma <- 0
		Para i <- 1 Hasta n Con Paso 1 Hacer
			suma <- suma + i
		FinPara
		Escribir 'La suma de los numeros de 1 a ' n ' es : " suma
	SiNo
		Escribir 'Por favor, ingresa un numero positivo'
	FinSi
FinAlgoritmo
