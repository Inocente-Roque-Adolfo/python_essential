print('Ejercicio02 - Agregar')
fruits = {"manzana":5, "peras":2, "naranjas":4}
print(f'Las frutas son: {fruits}\,')

#agregar bananas = 6, mangos = 1, uvas = 3
fruits['bananas'] = 6
print(f'Se agrego bananas: {fruits}')

fruits.setdefault('mangos',1)
print(f'Se agrego mangos: {fruits}')

fruits.update({'uvas':3})
print(f'Se agrego uvas: {fruits}')