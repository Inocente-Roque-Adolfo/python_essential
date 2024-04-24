diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#recorriendo el diccionario con un ciclo for
print('Las keys son: ', end='')
for clave in diccionario:
    print(clave, end='-')

print('\nLas keys son: ', end='')
for clave in diccionario.keys():
    print(clave, end='-')

print('\nLos valores son: ', end='')
for valor in diccionario.values():
    print(valor, end='-')

print('\nLos items son: ', end='')
for item in diccionario.items():
    print(item, end='-')
    