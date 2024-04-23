print('\n==============================\nDETERMINAR SI UN NUMERO ES PAR O IMPAR\n==============================\n')

print('** s = salir\n')

opcion = input("Introduce un número entero: ")

while opcion != 's':
    if opcion == 'c':
        opcion = input("Introduce un número entero: ")
        if opcion == 's':
            break
        
    if not opcion.isdigit():
        print('Por favor, introduce un número entero')
        opcion = 'c'
        continue

    opcion = int(opcion)
    if opcion % 2 == 0:
        print(f"El número {opcion} es par")
    else:
        print(f"El número {opcion} es impar")
    opcion = 'c'

print('terminado...')