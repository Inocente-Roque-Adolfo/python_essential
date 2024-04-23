#hello hola 
# traduce con python
#
#
cantidad_filas = int(input('Cuantas filas temdra la matriz? '))
cantidad_columnas = int(input('Cuantas columnas temdra la matriz? '))
matriz = []

print('\nIntroduce los elementos: ')
for row in range(cantidad_filas):
    for element in range(cantidad_columnas):
        filas = []
        matriz.append(filas)
        entero = input(f'Ingrese el elemento {row}x{element}: ')
        matriz[row].append(entero)
        
#Impresion
print('\nTu matriz es la siguiente'.center(20,'='))
for row in matriz:
    for element in row:
        print(element, end=' ')
    print('')







