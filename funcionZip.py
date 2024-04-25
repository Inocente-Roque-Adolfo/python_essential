#funcion zip
'''
La función zip() recibe dos o más objetos iterables 
(listas, tuplas, etc.) y devuelve un nuevo iterable 
cuyos elementos son tuplas que contienen un elemento 
de cada uno de los iterables originales. El nuevo iterable 
tiene tantos elementos como elementos tenga el iterable más corto.

'''

#Ejemplo 1
#Creando dos listas
lista1 = [1,2,3]
lista2 = [4,5,6]
#Creando una lista de tuplas
combinacion = list(zip(lista1,lista2))
print(combinacion) #[(1, 4), (2, 5), (3, 6)]

#Ejemplo 2
#Creando dos tuplas
names = ('John', 'Lisa', 'Terminator')
ages = [25, 30, 35]
datos_personales = zip(names, ages) #<zip object at 0x7f2b3a7f3f40>
print(list(datos_personales)) #[('John', 25), ('Lisa', 30), ('Terminator', 35)]

#Ejemplo 3
#Diccionario con los datos de los empleados
empleados = {'Juan': 25, 'Maria': 30, 'Pedro': 35}
#Creando una lista de tuplas
datos_personales = list(zip(empleados.keys(), empleados.values()))
print(datos_personales) #[('Juan', 25), ('Maria', 30), ('Pedro', 35)]

#Ejemplo 4
#incompleto 
frutas = ['manzana', 'pera', 'uva']
costos = (2, 3, 4, 5, 6)
jugo = zip(frutas, costos)
print(list(jugo)) #[('manzana', 2), ('pera', 3), ('uva', 4)]

#Ejemplo 5
#Juntar tres listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
combinacion = list(zip(lista1,lista2,lista3))
print(combinacion) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#Ejemplo 6
#Listas de 1 elemento vacio
lista1 = []
lista2 = [4]
combinacion = list(zip(lista1,lista2))
print(combinacion) #[(1, 4)]

#Ejemplo 7
#recorrer la lista con el ciclo for en zip 
names = ('John', 'Lisa', 'Terminator')
ages = [25, 30, 35]
for names, ages in zip(names, ages):
    print(names,'=>',ages)

#Ejemplo 8
#con string
names = 'John', 'Lisa', 'Terminator'
ages = [25, 30, 35]
string_asignado = "Terminator"
combinacion  = list(zip(names, ages, string_asignado))
print(combinacion) #[('John', 25, 'T'), ('Lisa', 30, 'e'), ('Terminator', 35, 'r')]

#Ejemplo 9
#quitar list y convertir a tupla
names = ('John', 'Lisa', 'Terminator')
ages = [25, 30, 35]
string_asignado = "Terminator"
datos_personales = zip(names, ages, string_asignado)
print(tuple(datos_personales)) #(('John', 25), ('Lisa', 30), ('Terminator', 35))


