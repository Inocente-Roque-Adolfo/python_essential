#diccionarios 
nombre_diccionario = {}
print(nombre_diccionario)

nombre_diccionario = {'key': 'elemento', 'key1': 'elemento2'}
print(nombre_diccionario)

#acceder
dato1 = nombre_diccionario['key']
print(dato1)


#modificar
nombre_diccionario['key'] = 'elemento3'
print(nombre_diccionario)

#agregar
nombre_diccionario['key2'] = 'elemento4'
print(nombre_diccionario)

nombre_diccionario['key3'] = 'elemento5'
print(nombre_diccionario)

#recorrer
for key in nombre_diccionario:
    print(key)

#items() devuelve una lista de tuplas con clave y valor 
nombre_diccionario.items()
print(nombre_diccionario.items())
lista = list(nombre_diccionario.items())
print(lista)

#keys() devuelve una lista de las claves
nombre_diccionario.keys()
print(nombre_diccionario.keys())
lista = list(nombre_diccionario.keys())
print(lista)

#values() devuelve una lista de los valores
nombre_diccionario.values()
print(nombre_diccionario.values())
lista = list(nombre_diccionario.values())
print(lista)

#clear() elimina todos los elementos del diccionario pero no elimina el diccionario
nombre_diccionario.clear()
print(nombre_diccionario)


#eliminar
del nombre_diccionario
#print('\n',nombre_diccionario)


