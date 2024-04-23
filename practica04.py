print('\n=====================\nCalculadora\n=====================\n******************\n*Menu de opciones*\n******************\n')

print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Division entera\n6. Modulo o Resto\n7. Potencia\n8. Salir\n')
while True:
    try:
        numero = int(input('* Ingrese la opcion deseada: '))
        break
    except ValueError:
        print('Error: Ingrese una opcion valida')
        continue


while numero != 8:
    if numero == "c":
        print('\n=====================\nCalculadora\n=====================\n******************\n*Menu de opciones*\n******************\n')
        print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Division entera\n6. Modulo o Resto\n7. Potencia\n8. Salir\n')
        while True:
            try:
                numero = int(input('* Ingrese la opcion deseada: '))
                break
            except ValueError:
                print('Error: Ingrese una opcion valida')
                continue

        if numero == 8:
            break
    
    # Suma 
    if numero == 1:
        print('\n******************\nEscogio la opcion de suma\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero += float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La suma es: {numero}')
    # Resta
    elif numero == 2:
        print('\n******************\nEscogio la opcion de resta\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero -= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La resta es: {numero}')
    
    # Multiplicacion
    elif numero == 3:
        print('\n******************\nEscogio la opcion de multiplicacion\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero *= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La multiplicacion es: {numero}')

    # Division
    elif numero == 4:
        print('\n******************\nEscogio la opcion de division\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero /= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La division es: {numero}')

    # Division entera
    elif numero == 5:
        print('\n******************\nEscogio la opcion de division entera\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero //= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La division entera es: {numero}')

    # Modulo o Resto
    elif numero == 6:
        print('\n******************\nEscogio la opcion de modulo o resto\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero %= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'El modulo o resto es: {numero}')

    # Potencia
    elif numero == 7:
        print('\n******************\nEscogio la opcion de potencia\n')
        while True:
            try:
                numero = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        while True:
            try:
                numero **= float(input('Ingrese el segundo numero: '))
                break
            except ValueError:
                print('Error: Ingrese un numero valido')
                continue
        print(f'La potencia es: {numero}')
    # Salir
    elif numero == 8:
        print('Saliendo del programa...')
    else:
        print('Opcion invalida')
    numero = "c"    
print('Saliendo del programa...')




