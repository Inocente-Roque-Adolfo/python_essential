print('Conversor de letras a números \n')
print('=============================')
print('Menu de opciones:')
print('1) convertir de numero a letras')
print('2) convertir de letra a numero')
print('============================= \n')

numeroElegido = int(input("Cual es tu opción? "))

if numeroElegido == 1:
    numero = int(input("Introduce un número: "))
    if numero == 1:
        print("El número",numero,"en letras es: UNO")
    elif numero == 2:
        print("El número",numero,"en letras es: DOS")
    elif numero == 3:
        print("El número",numero,"en letras es: TRES")
    elif numero == 4:
        print("El número",numero,"en letras es: CUATRO")
    elif numero == 5:
        print("El número",numero,"en letras es: CINCO")
    else:
        print("Número no registrado")
elif numeroElegido == 2:
    palabra = input("Introduce una letra: ")
    if palabra == 'uno' or palabra == 'UNO' or palabra == 'Uno':
        print("La letra",palabra,"en numeros es: 1")
    elif palabra == 'dos' or palabra == 'DOS' or palabra == 'Dos':
        print("La letra",palabra,"en numeros es: 2")
    elif palabra == 'tres' or palabra == 'TRES' or palabra == 'Tres':
        print("La letra",palabra,"en numeros es: 3")
    elif palabra == 'cuatro' or palabra == 'CUATRO' or palabra == 'Cuatro':
        print("La letra",palabra,"en numeros es: 4")
    elif palabra == 'cinco' or palabra == 'CINCO' or palabra == 'Cinco':
        print("La letra",palabra,"en numeros es: 5")
    else:
        print("Número no registrado")

else:
    print("Opción no válida")
    