# Desempaquetar tuplas
# Desempaquetar tuplas es una técnica que permite asignar los valores de una tupla a variables individuales.

# Ejemplo:
# En este caso, la tupla contiene tres elementos y 
# se asignan a las variables a, b y c respectivamente.
tupla = (1, 2, 3)
a, b, c = tupla
print(a)  # 1
print(b)  # 2
print(c)  # 3

vocales = ('a', 'e', 'i', 'o', 'u')
# v1, v2, v3, v4 = vocales # error porque hay menos variables que elementos en la tupla
v1, v2, v3, v4, v5 = vocales
print(v1)  # a
print(v2)  # e
print(v3)  # i
print(v4)  # o
print(v5)  # u

#tuplas inmutables
# Las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.
# Si intenta modificar una tupla, se generará un error.
# Ejemplo:
tupla = (1, 2, [3, 4],{'a':1})
#tupla[0] = 100  # error
tupla[2][0] = 300
print('modifique tupla[2][0] = 300  "(1, 2, [3, 4])"',tupla)  # (1, 2, [300, 4])
tupla[3]['a'] = 100
print('modifique tupla[3][\'a\'] = 100  "(1, 2, [300, 4],{\'a\':1})"',tupla)  # (1, 2, [300, 4],{'a':100})


"""
este es 
un comentario
de varias lineas
con comillas dobles
"""
'''
Este es
un comentario
de varias lineas
con comillas simples
'''





