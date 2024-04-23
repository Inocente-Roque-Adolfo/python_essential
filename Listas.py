# Description: Ejemplos de listas en Python
# pop - elimina el ultimo elemento de la lista
# append - agrega un elemento al final de la lista
# insert - agrega un elemento en la posicion indicada
# extend - agrega los elementos de la lista al final
# count - cuenta cuantas veces se repite un elemento
# index - devuelve la posicion de un elemento - la primera vez que lo encuentra
# len - devuelve la longitud de la lista
# remove - elimina un elemento de la lista - la primera vez que lo encuentra
# reverse - invierte los elementos de la lista 
# sort - ordena los elementos de la lista
# clear - limpia la lista
# del - elimina un elemento o la lista completa
#




#Lista vacia
lista =[]

#Listas homogenea = lista de un solo tipo de dato
lista_homogenea = [1,2,3,4,5,6,7,8,9,10]
lista_homogenea = ["Javier", "Luis", "Pedro", "Juan", "Maria", "Ana", "Luisa", "Carlos", "Jose"]

#Listas heterogeneas
lista_heterogenea = [1,"Javier", True, 3.14]

#Listas multidimensionales
lista_multidimensional = [[1,2,3],[4,5,6],[7,8,9]]
#print(lista_multidimensional[1][0])

#Listas de tuplas
lista_tuplas = [(1,2,3),(4,5,6),(7,8,9)]
#print(lista_tuplas[1][0])

#Listas de diccionarios
lista_diccionarios = [{"nombre":"Javier", "edad": 23},{"nombre":"Luis", "edad": 24},{"nombre":"Pedro", "edad": 25}]
#print(lista_diccionarios[2]["nombre"])

#Listas de conjuntos
lista_conjuntos = [{1,2,3},{4,5,6},{7,8,9}]

valores_booleanos = [True, False, True, False, True, False]
print(valores_booleanos)
print(valores_booleanos.count(False))
print(valores_booleanos.count(True))

string = "Hola mundo"
print(string[0:4])

enteros = [1,2,3,4,5,6,7,8,9,10]
print('Hay en enteros',len(enteros),'elementos y el numero',enteros[0:10:2],' con posicion:', enteros.index(len(enteros)))
#posiciones
#print(enteros[11])
print(enteros[9])

enteros[9] = 100
print(enteros[9])

#enteros[:] = '0'
print(enteros[:])

#enteros[:]+= 2 # no se puede 
print(enteros[:])

enteros = [1,2,3,4,5,6,7,8,9,10]
enteros.append(11)
print(enteros[:])
print('dato agregado con .append(11)',enteros[10])

print('\ninsert')
print(enteros)
#insert recibe dos parametros, el primero es la posicion y el segundo el valor
enteros.insert(0,0)
print('dato agregado con .insert(0,0)',enteros[0])
print(enteros)

print('\npop')
print(enteros)
print('dato eliminado con .pop() =>',enteros[11])
enteros.pop() #elimina el ultimo elemento
print(enteros)
print('dato eliminado con .pop(1) =>',enteros[1])
enteros.pop(1) #elimina el elemento en la posicion 1
print(enteros)

print('\nextend')
print(enteros)
print('dato agregado con .extend([11,12,13,14,15])',enteros[10:15])
enteros.extend([11,12,13,14,15]) #agrega los elementos de la lista al final
print(enteros)
#falta el numero 1 borrado con el pop
enteros.insert(1,1)
print('falla en la posicion 1=>',enteros[1])
print(enteros)

print('\nIndex')
enteros.index(1)
print(enteros)
print('posicion del 1:',enteros.index(1))
print('cantidad de elementos:',len(enteros))
vocales = ['a', 'e', 'i', 'a','o', 'u','a']
print(vocales)
print('posicion de la vocal "a":',vocales.index('a'))
print('posicion de la segunda vocal "a":',vocales.index('a',1)) #busca a partir de la posicion 1
print('posicion de la tercera vocal "a":',vocales.index('a',4, 7)) #busca a partir de la posicion 4

print('\nRemove')
print(enteros)
print('dato eliminado con .remove(2)=>',enteros[2])
enteros.remove(2) #elimina el elemento 2 #elimina solo elementos que se encuentren en la lista
print(enteros)

print('\nReverse')
enteros.insert(2,2)
print(enteros)
print('datos invertidos con .reverse()') #invierte los datos
enteros.reverse()
print(enteros)
enteros.reverse()
print(enteros)
vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales)
vocales.reverse()
print(vocales)

print('\nSort')
lista_Desordenada = [5,3,1,4,2]
vocales_Desordenadas = ['u','o','i','e','a']
letras_Desordenadas = ['z','y','x','w','v'] 
print(lista_Desordenada)
lista_Desordenada.sort() #ordena la lista
print('ascendente sort() =>',lista_Desordenada)
lista_Desordenada.sort(reverse=True) #ordena la lista de forma descendente
print('descendente sort(reverse=True) =>',lista_Desordenada)
print(vocales_Desordenadas)
vocales_Desordenadas.sort() #ordena la lista
print('ascendente sort() =>',vocales_Desordenadas)
vocales_Desordenadas.sort(reverse=True) #ordena la lista de forma descendente
print('descendente sort(reverse=True) =>',vocales_Desordenadas)
print(letras_Desordenadas)
letras_Desordenadas.sort() #ordena la lista
print('ascendente sort() =>',letras_Desordenadas)
letras_Desordenadas.sort(reverse=True) #ordena la lista de forma descendente
print('descendente sort(reverse=True) =>',letras_Desordenadas)


print('\nClear')
print(enteros)
enteros.clear() #limpia la lista pero no la elimina
print(enteros)

print('\nDel')
enteros = [0,1,2,3,4,5,6,7,8,9,10]
print(enteros)
del enteros[0] #elimina el elemento en la posicion 0
print(enteros)
del enteros[0:5] #elimina los elementos en el rango 0-5
print(enteros)
del enteros[:] #limpia la lista pero no la elimina
print(enteros)
del enteros #elimina la lista por completo
#print(enteros) #error porque la lista fue eliminada


#extend
print('\nExtend')
enteros = [0,1,2,3,4,5,6,7,8,9,10]
print(enteros)
enteros.extend([11,12,13,14,15]) #agrega los elementos de la lista al final
print(enteros)
enteros.extend([16,17,18,19,20]) #agrega los elementos de la lista al final
print(enteros)
agregar = [21,22,23,24,25]
enteros.extend(agregar) #agrega los elementos de la lista al final
print(enteros)
enteros.extend('Hola') #agrega los elementos de la lista al final
print(enteros)
enteros.extend(range(5,100,2)) #agrega los elementos de la lista al final
print(enteros)


#sum(objeto_iterable, valor_inicial)
print('\nSum')
enteros = [0,1,2,3,4,5,6,7,8,9,10]
print(enteros)
print('suma de los elementos de la lista:',sum(enteros))
print('suma de los elementos de la lista +100:',sum(enteros, 100)) #suma los elementos de la lista y le agrega 100
print(enteros)
print('suma de los elementos de la lista +10:',sum(enteros, 10)) #suma los elementos de la lista y le agrega 10
print('resta',sum(enteros, -10)) #suma los elementos de la lista y le resta 10

#suma lista heterogenea
lista_heterogenea = [1, True]
print(lista_heterogenea)
#suma de los elementos de la lista
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum(lista_heterogenea))




