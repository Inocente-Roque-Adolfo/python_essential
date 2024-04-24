#Eliminina el ultimo item del diccionario y lo devuelve como una tupla

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
item = diccionario.popitem()
print(item)

print(diccionario) # {'a': 1, 'b': 2, 'c': 3}

# Si el diccionario esta vacio, se genera un error
diccionario = {}
item = diccionario.popitem()
print(item) # KeyError: 'popitem(): dictionary is empty'


