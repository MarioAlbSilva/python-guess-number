import random

print("JUEGO DE ADIVINAR UN NUMERO")
print("El objetivo es adivinar un número entre 1 y 30.")
print("Se tiene 8 intentos para adivinarlo.")

numero_oculto = random.randint(1, 30)
intentos = 8
continuar = True

while continuar:
	while intentos > 0:
		try:
			numero = int(input("Ingrese un número:"))

			if numero == numero_oculto:
				print("Correcto, ha ganado")
				break
			elif numero > numero_oculto:
				print("El número ingresado es mayor.")
			elif numero < numero_oculto:
				print("El número ingresado es menor.")

			intentos -= 1
		except:
			print("El valor no es un número.")

	if intentos == 0:
		print("Se acabaron los intentos, juego terminado.")

	opcion = ''

	while opcion != 'Y' or opcion != 'N':
		opcion = input("¿Desea volver a intentarlo? Y/N:")

		if opcion.lower() == 'y':
			numero_oculto = random.randint(1, 30)
			intentos = 8
			break
		elif opcion.lower() == 'n':
			print("Gracias por jugar, vuelva pronto.")
			continuar = False
			break
