#Recorrido de una tupla 
tuple_n = (1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15)

print(tuple_n)
for indice in tuple_n:
    print(indice)


#desempaquetar tuplas
for n1, n2, n3, n4, n5 in tuple_n:
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)

#Funcion tuple con diccionario
dict_Claves = dict(a=1, b=2, c=3, d=4, e=5)
print(dict_Claves)
tupla_Claves = tuple(dict_Claves)
print(tupla_Claves)

tuple_valores = tuple(dict_Claves.values())
print(tuple_valores)

#cordenadas
x = 10
y = 20

coordenadas = tuple([x, y])
print(coordenadas)

#string
string = 'Hola'
tupla_string = tuple(string)
print(tupla_string)

#lista == tuple([1, 2, 3, 4, 5])
lista = [1, 2, 3, 4, 5]
tupla_lista = tuple(lista)
print(tupla_lista)

#range
rango = range(1, 10)
tupla_rango = tuple(rango)
print(tupla_rango)



