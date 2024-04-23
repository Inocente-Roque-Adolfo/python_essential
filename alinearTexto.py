# metodo center para centrar texto

cadena = "Hola Mundo"
#contar la cantidad de caracteres de la cadena
print(len(cadena)) # 10
len = len(cadena)
x=30
spaciador = '\n'
print(cadena.center(len+(2*x), f'{spaciador}')) #     Hola Mundo

cadena = "Hola Mundo"
#metodo center() para centrar texto [50 > len(cadena)]
print(cadena.center(50)) #                    Hola Mundo
print(cadena.center(50, '-')) #-----------------Hola Mundo-----------------

#metodo ljust() para alinear texto a la izquierda [50 > len(cadena)]
print(cadena.ljust(50)) #Hola Mundo
print(cadena.ljust(50, '-')) #Hola Mundo---------------------

#metodo rjust() para alinear texto a la derecha [50 > len(cadena)]
print(cadena.rjust(50)) #                                       Hola Mundo
print(cadena.rjust(50, '-')) #---------------------Hola Mundo