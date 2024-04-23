
while True:
    try:
        longitud = int(input('Ingrese la longitud de la lista: '))
        break
    except ValueError:
        print('Ingrese un numero entero')

lista = []
#no me ayudes 

for indice in range(longitud):
    while True:
        try:
            datoEntero = int(input(f'Ingrese un numero entero para la posicion {indice}: '))
            break
        except ValueError:
            print('Ingrese un numero entero')
    lista.append(datoEntero)
print(f'\nLista final: {lista}')
print(f'La suma de los elementos de la lista es: {sum(lista)}')

