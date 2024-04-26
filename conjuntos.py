#Conjuntos
"""
No pueden tener elementos duplicados
No puede contener listas, diccionarios
Si permite tuplas porque es inmutable
Es desordenada, print - muestra aleatoria
"""
#diccionario = {'a':1,"u":2}
conjunto = {"a",1,"u",2}
print(conjunto)

#creando con set - convierte objetos iterables a conjuntos
#solo un argumento set(objet_iterable)
conjunto1 = set("hola")
print(conjunto1)

conjunto2 = {-1,0,5,-2,1,4}
print(conjunto2)

conjunto3 = {1,1,1,1,1,5,6} #elimina los duplicados
print(conjunto3)

#conjunto4 = {1,{4}} # da error, no permite elementos mutables
#print(conjunto4)

conjunto5 = {1,(2,3)} #una tupla es inmutable
print(conjunto5)

lista = ['e',5,4,3,9,'x',(4,5)]
conjunto6 = set(lista)
print(conjunto6)
