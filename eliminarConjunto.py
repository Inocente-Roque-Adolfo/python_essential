#Eliminar elementos de conjuntos
# metodo: remove()
"""
Si no encuentra el elemento da error key
solo un argumento
remove() solo elimina un elemento
"""
vocales = {'a','e','i','o','u'}
print(vocales,'\n')
vocales.remove('a')
print(f'Eliminado la vocal a con remove(): {vocales}')

#vocales.remove('a')
print(f'Eliminar nuevamente a con remove(): {vocales} => Da error')

# metodo: discard()
"""
Si no encuentra el elemento no da error
solo un argumento
"""
vocales = {'a','e','i','o','u'}
vocales.discard('a')
print(f'Eliminado la vocal a con discard(): {vocales}')

vocales.discard('a')
print(f'Intente eliminar la vocal a con discard(): {vocales} => No da error')


print('\n\n====Evitar error remove con condicionales====')
vocales = {'a','e','i','o','u'}
elemento = 'z'
if elemento in vocales:
    vocales.remove(elemento)
    print('resultado:',vocales)
else: 
    print(elemento,'no esta en el conjunto vocales')