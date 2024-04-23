# metodo count() - retorna la cantida de veces que um elemento aparece en una lista 

cadena = "Hola Mundo"
print(cadena.count('H')) # 1
print(cadena.count('o')) # 2
print(cadena.count('l')) # 1
print(cadena.count('a')) # 1
print(cadena.count(' ')) # 1
print(cadena.count('M')) # 1
print(cadena.count('u')) # 1
print(cadena.count('n')) # 1
print(cadena.count('d')) # 1
print(cadena.count('o')) # 2

print('\n')
# Si se busca una cadena de caracteres que no existe en la cadena, el metodo count() retorna 0
print(cadena.count('')) # 11
print(cadena.count('s')) # 0
print(cadena.count('Hola Mundo')) # 1
print(cadena.count('Hola')) # 1
print(cadena.count('Mundo')) # 1

print('\n')
cadena = 'Mi mama me mima'
print(cadena.count('m')) # 5
print(cadena.count('M')) # 1 
print(cadena.count('mi')) # 1
print('\n')
entero = 1234567891111
# El metodo count() no se puede aplicar a un tipo de dato enteros
#convertir a cadena de caracteres
cadena = str(entero)
print(cadena.count('1')) # 1

print('\n')
cadena = "Hola Mundo"
# Se puede especificar un rango de busqueda
print(cadena.count('o', 2)) #segunda o
print(cadena.count('o', 2, 9)) 
print(cadena.count('o', -10))
print(cadena.count('o', -10, -1)) # penultima o


#parte practica
cadena = "Mi mama me mima mucho a mi"
len = len(cadena)
cadena = cadena.center(len+(2*5), '*')
print(cadena) # ***Hola Mundo*****
contador = cadena.count('m')
print('Hay', contador, 'm en minuscula la cadena') # Hay  7 m en la cadena
print('Hay', cadena.count('M'), 'M en mayuscula en la cadena') # Hay  1 M en la cadena
