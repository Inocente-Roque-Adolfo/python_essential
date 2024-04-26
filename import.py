#Intruccion import
"""
pYTHON da diversos modulos
"""
#Modulo completo math
import math
print(math.sqrt(64))

#Modulo math con alias
import math as m
print(m.sqrt(25))

#Traes solo algunas funciones
from math import sqrt, sin
print(sqrt(36))
#print(tan(36))  da error

#Importar todo el modulo (todas las funciones disponibles) (evitar)
from math import *
print(sqrt(36))
print(tan(36))
print(sin(36))




