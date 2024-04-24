#metodo pop

#pop() remove o último item da lista e o retorna

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(diccionario)
item = diccionario.pop('a')
print(item)
print(diccionario) # {'b': 2, 'c': 3, 'd': 4}

# Si la clave no existe, se genera un error
#item = diccionario.pop('z') # KeyError: 'z'
item = diccionario.pop('z', '"z" No existe')
print(item) # No existe


#con listas
lista = [1, 2, 3, 4]
print('\n',lista)
item = lista.pop()
print(item)
print(lista) # [1, 2, 3]