#metodo update
# El método update() actualiza el diccionario con elementos de 
#                    otro diccionario o con una secuencia de pares clave-valor.

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(diccionario,'\n')

# Actualizar el diccionario con nuevos datos
diccionario.update({'e': 5, 'f': 6})
print('Agregando "e" y "f":\n',diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

#modificar un valor
diccionario.update({'a': 10})
print('Modificando el valor de "a":\n',diccionario,'\n')  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


# Actualizar el diccionario con un diccionario vacío
diccionario.update({})
print('Actualizando con un diccionario vacío:\n',diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Actualizar el diccionario con una secuencia de pares clave-valor
diccionario.update([('g', 7), ('h', 8)])
print('Actualizando con una secuencia de pares clave-valor:\n',diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


