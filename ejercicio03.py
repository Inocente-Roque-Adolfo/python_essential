print('Ejercicio03 - Eliminar')
fruits = {"manzana":5, "peras":2, "naranjas":4}
print(f'Las frutas son: {fruits}')

#forma de eliminar peras
fruits.pop('peras')
print(fruits)

#segunda forma de eliminar naranjas
del fruits['naranjas']
print(fruits)