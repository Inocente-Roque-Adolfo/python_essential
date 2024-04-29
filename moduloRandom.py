#Modulo Random
#import random
#print(random.randint(0,100))

#funcion randint ( ) , devuelve un entero aleatorio en eI rango [e, b]
#e ->limite inferior
#b ->limite superior

#a<=N<=b
from random import randint as variable
print('Numero aleatorio randint(): ',variable(0,100))

#funcion random( ), devuelve un numero de punto flotante en el rango[0.0,1.0]
#0.0<=N<1.0
from random import random as random
print('Numero aleatorio random(): ',random())

#funcion randrange(), devuelve un elemento aleatorio de la secuencia 
#                     generada por range(start,stop,step) a<=N<b

from random import randrange
print('Numero aleatorio randrange(): ',randrange(0,100,2))
