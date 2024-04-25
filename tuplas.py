#Tuplas
#**Creadas no se pueden modificar
#**Se pueden acceder a los elementos de la tupla mediante el uso de índices
#**Se pueden concatenar tuplas

#Creación de tuplas
tupla0 = (1) #Esto no es una tupla ya que no tiene una coma
print('Esto no es una tupla ya que no tiene una coma "tupla0 = (1)": ',tupla0,'\n')

tupla = 1,2,3,4,5
print('Tupla creada sin parentesis "tupla = 1,2,3,4,5": ',tupla,'\n')

tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10)
tupla3 = tupla1 + tupla2
print('La suma de "tupla1 = (1,2,3,4,5)" + "tupla2 = (6,7,8,9,10)" = ',tupla3,'\n')

#No se pueden modificar los elementos de una tupla
nueva_tupla = (1,2,3,4,5)
#nueva_tupla[0] = 10 #Esto generará un error

#Tuplas anidadas
tupla_anidada = (1,2,3,(4,5,6))
print('Tupla anidada "tupla_anidada = (1,2,3,(4,5,6))": ',tupla_anidada,'\n')

#Tupla vacía
tupla_vacia = ()
print('Tupla vacía "tupla_vacia = ()": ',tupla_vacia, end=' ')
print(type(tupla_vacia),'\n')

#Tupla homogénea
tupla_homogenea = (1,2,3,4,5)
print('Tupla homogénea: ',tupla_homogenea,'\n')

#Tupla heterogénea
tupla_heterogenea = (1,'hola',3.14)
print('Tupla heterogénea: ',tupla_heterogenea,'\n')

#Tupla sin paréntesis
tupla_sin_parentesis = 1,2,3,4,5
print('Tupla sin paréntesis "tupla_sin_parentesis = 1,2,3,4,5": ',tupla_sin_parentesis,'\n')

#Tupla de un solo elemento
tupla_un_elemento = (1,)
print('Tupla de un solo elemento "tupla_un_elemento = (1,)": ',tupla_un_elemento,'\n')


#accede a los elementos de la tupla mediante el uso de índices
tupla = (1,2,3,4,5)
print('Elemento en la posición 0 de la tupla "tupla = (1,2,3,4,5)": ',tupla[0],'\n')
print('Elemento en la posición 1 de la tupla "tupla = (1,2,3,4,5)": ',tupla[1],'\n')
print('Elemento en la posición 2 de la tupla "tupla = (1,2,3,4,5)": ',tupla[2],'\n')
print('Elemento en la posición 3 de la tupla "tupla = (1,2,3,4,5)": ',tupla[3],'\n')
print('Elemento en la posición 4 de la tupla "tupla = (1,2,3,4,5)": ',tupla[4],'\n')
print('Elemento en la posición -1 de la tupla "tupla = (1,2,3,4,5)": ',tupla[-1],'\n')
#print('Elemento en la posición 5 de la tupla "tupla = (1,2,3,4,5)": ',tupla[5],'\n') #error tuple index out of range

#Segmentacion 
tupla = (1,2,3,4,5)
print('Segmento de la tupla (1,2,3,4,5) "tupla[1:4]": ',tupla[1:4],'\n')

#con saltos
tupla = (1,2,3,4,5)
print('Segmento de la tupla (1,2,3,4,5) con saltos "tupla[1:4:2]": ',tupla[1:4:2],'\n')