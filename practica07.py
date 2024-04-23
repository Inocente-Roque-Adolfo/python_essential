palabra = input("Digite uma palabra: ")

cantidad_letras = len(palabra)

#imprimir al reves
#range (inicio, fin, paso)adolfo = 6
print('La palabra al reves es: ', end='')
for i in range(cantidad_letras-1, -1, -1):
    
    #rango va desde la cantidad de letras -1 hasta antes de -1
    print(palabra[i], end="")

print('\nFin del programa')

palabra = range(cantidad_letras-1, -1,)
print(palabra)

#0a1d2o3l4f5o6
#-6a-5d-4o-3l-2f-1o0

#5 4 3 2 1 0 -1
#    = 3
#3-1 = 2
#2-1 = 1
#1-1 = 0
#0-1 = -1 # no se imprime porque es el final del rango
# el rango se considera el inicio pero no el final 

