print('\n==============================\nDETERMINAR EL NUMERO MAYOR\n==============================\n')
print('** e = empezar')
print('** s = salir\n')

opcion = input("Introduce una opción: ")

while opcion != 's':
    if opcion == 'c':
        print('\n\n==============================\nDETERMINAR EL NUMERO MAYOR\n==============================\n')
        print('** e = continuar')
        print('** s = salir\n')
        opcion = input("Introduce una opción: ")
        if opcion == 's':
            break

    if opcion == 'e':
        print('\n========================\n')
        while True:
            try:
                primer_numero = float(input("Introduce el primer numero: "))
                break
            except ValueError:
                print("Por favor, introduce un número") 
        while True:
            try:
                segundo_numero = float(input("Introduce el segundo numero: "))
                break
            except ValueError:
                print("Por favor, introduce un número")
        while True:
            try:
                tercer_numero = float(input("Introduce el tercer numero: "))
                break
            except ValueError:
                print("Por favor, introduce un número")

        print('\n *******************\n ')
        if primer_numero > segundo_numero and primer_numero > tercer_numero:
            print(f"El número mayor es: {primer_numero}")
        elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
            print(f"El número mayor es: {segundo_numero}")
        elif tercer_numero > primer_numero and tercer_numero > segundo_numero:
            print(f"El número mayor es: {tercer_numero}")
        else:
            print("Los números son iguales")
        print('\n *******************\n ')
        opcion = 'c'
    else:
        opcion = input("Introduce una opción valida('e' 's'): ")
        
print('terminado...')



