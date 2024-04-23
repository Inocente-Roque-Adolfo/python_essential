while True:
    #Cuantas matrices vas a sumar
    try:
        cantidad_matrix = int(input('Cuantas matrices vas a sumar: '))
    except ValueError:
        print('ingrese numeros enteros')
    if cantidad_matrix<=1:
        print('Se necesitan 2 o mas para realizar la suma')
    else:
        break

#Cuantas filas y columnas tendra
while True:
    #Cuantas matrices vas a sumar
    try:
        dimension = int(input('Cuantas filas y columnas tendran: '))
    except ValueError:
        print('ingrese numeros enteros')
    if cantidad_matrix<=1:
        print('solo numeros mayores o iguales a 2')
    else:
        break


matriz_General =  []



#crear matices n
for CantidadMatriz in range(cantidad_matrix):
    print(f'Datos de la matriz {CantidadMatriz+1}')
    #Crear la matriz a ingresar a la matriz general
    matriz_Nueva = []
    for fila in range(dimension):
        filaNueva = []
        matriz_Nueva.append(filaNueva)
        for columna in range(dimension):
            matriz_Nueva[fila].append(int(input(f'Ingrese el dato {fila}x{columna}: ')))
    matriz_General.append(matriz_Nueva)

#sumarlos
temporal = []
matriz_suma = []
for row in range(dimension):
    lixta_nueva =[]
    for colum in range(dimension):
        for num_Matriz in range(cantidad_matrix):
            temporal.append(matriz_General[num_Matriz][row][colum]) 
            if len(temporal)==cantidad_matrix:
                lixta_nueva.append(sum(temporal))
                #print(sum(temporal))
                temporal.clear()
    matriz_suma.append(lixta_nueva)

#impresion resultado
for row in range(len(matriz_suma)):
    print(f'{matriz_suma[row]}')


for row in range(dimension):
    for colum in range(dimension):
        print(matriz_suma[row][colum], end=' ')
    print('')

print(matriz_suma)











#[#matriz] [#fila] [#columna]

#print(matriz_General)
#PRIMERA MATRIZ
#print(matriz_General[0])

#Primera fila de la primera matriz
#print(matriz_General[0][0]) #print(matriz_General[0][1])

#Primer elemento de la primera fila de la primera matriz
#print(matriz_General[0][0][0])

#SEGUNDA MATRIZ
#print(matriz_General[1])

#suma el primer elemento 0x0
#print(matriz_General[0][0][0] + matriz_General[1][0][0])

#suma el segundo elemento 0X1
#print(matriz_General[0][0][1] + matriz_General[1][0][1])

#suma el tercer elemento 0X2
#print(matriz_General[0][0][2] + matriz_General[1][0][2])
