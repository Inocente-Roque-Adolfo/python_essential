names_tuples = ('Ana', 'Gerardo', 'Maria', 'Carlos', 'Valentina')
print('Tupla original:', names_tuples)
extension = len(names_tuples)-1

""" #No se necesita en este caso porque debo pedir un número entre 0 y la extensión de la tupla
#Ejemplo 01: Mostrar el nombre correspondiente al índice ingresado
random = int(input(f'Ingrese un número entre 0-{extension}: '))
if random>=0 and random<=extension:
    print('Número válido')
    print(f'El nombre correspondiente al indice {random} es: {names_tuples[random]}')
else:
    print(f'Número inválido solo 0-{extension-1}')
    print('El programa ha finalizado')
"""

#Ejemplo 02: Mostrar el nombre correspondiente al índice ingresado
#           hasta que el número ingresado sea válido
print('\nEjemplo 02: Mostrar el nombre correspondiente al índice ingresado')
while True:
    random = int(input(f'Ingrese un número entre 0-{extension}: '))
    if random>=0 and random<=extension:
        print('\nNúmero válido')
        print(f'El nombre correspondiente al indice {random} es: {names_tuples[random]}')
        break
    else:
        print(f'\n¡ERROR! Número inválido')


