# Description 01: Eliminar un número existente en una tupla 
print('Ejemplo 01: Eliminar un número existente en una tupla')
nums_tuple = (5,8,3,3,1,6,2)
print(f'Tupla original: {nums_tuple}')

existente = int(input('Ingrese un número a existente a eliminar: '))

if existente in nums_tuple:
    convertido = list(nums_tuple)
    while existente in convertido:
        convertido.remove(existente)
    print(f'El número {existente} existe en la tupla')
    nums_tuple = tuple(convertido)
    print(f'Tupla modificada: {nums_tuple}')

else:
    print(f'El número {existente} no existe en la tupla')


# Description 02: Modificar por 0 un número existente en una lista
print('\nEjemplo 02: Modificar por 0 un número existente en una lista')
nums_tuple = (5,8,3,3,1,6,2)
print(f'\nTupla original: {nums_tuple}')

existente = int(input('Ingrese un número a existente a modificar por 0: '))

if existente in nums_tuple:
    print(f'El número {existente} existe en la tupla')
    cantidad = nums_tuple.count(existente)
    for i in range(cantidad):
        index = nums_tuple.index(existente)
        convertido = list(nums_tuple)
        convertido[index] = 0
        
        nums_tuple = tuple(convertido)
    print(f'Tupla modificada: {nums_tuple}')
else:
    print(f'El número {existente} no existe en la tupla')



