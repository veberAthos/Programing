def menu():
	print("######################")
	print("# CALCULADORA BASICA #")
	print("######################")
	
	print("\nSeleccione la operacion a realizar:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")

while True:
	menu()

	op = int(input("\nSeleccion: "))

	if op<1 or op>4:
		print ("\nSeleccion incorrecta")
		continue
	else:
		num1 = int(input("Ingrese el primer numero: "))
		num2 = int(input("Ingrese el segundo numero: "))

		if op == 1:
			res = num1 + num2
		elif op == 2:
			res = num1 - num2
		elif op == 3:
			res = num1 * num2
		elif op == 4:
			res = num1 / num2

		print ('El resultado es: {}'.format(res))
	reset = input('\nDesea realizar otra operacion? Y/N: ')
	if reset == 'N' or reset == 'n':
		break
