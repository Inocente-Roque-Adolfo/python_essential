#Expresiones de comprension
#syntax: [expresion for elemento in iterable if condicion]
"""
Lista de compresion
Conjunto de compresion
Diccionario de compresion: {nombre: edad for nombre, edad in personas if edad>=30}
"""
#Sin expresion
cuadrados = []
for elemento in range(10):
    cuad = elemento**2
    cuadrados.append(cuad)
print('Realizado sin expresiones de compresion: ',cuadrados)

cuadrados.clear()
for elemento in range(10):
    if elemento%2==0:
        cuad = elemento**2
        cuadrados.append(cuad)
print('Pares sin expresiones de compresion: ',cuadrados)



#Lista de compresion
#syntax: [expresion for elemento in iterable if condicion]
elevados = [x**2 for x in range(10)]
print('\nRealizado con expresiones de compresion: ',elevados)

elevados = [x**2 for x in range(10) if x%2==0 ]
print('Pares con CONDICION en expresiones de compresion: ',elevados)

elevados = [x**2 for x in range(0,10,2) ]
print('Pares en RANGO con expresiones de compresion: ',elevados)


#Diccionario de comprension
personas = [("carlos",30), ("gerardo",25),("maria",35)]
diccionarios_personas = {nombre: edad for nombre, edad in personas if edad>=30}
print('\n\nRealizado con Diccionario de compresion: ',diccionarios_personas)


