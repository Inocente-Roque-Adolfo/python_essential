
#for indice in 

#for(i=0; i<10; i++) #en python
for i in range(0,10,2):
    print(i)



primera_fila = [1, 2, 3]
segunda_fila = [4, 5, 6]
tercera_fila = [7, 8, 9]

matrix = [primera_fila, segunda_fila, tercera_fila]

for row in matrix:
    print(row)


for row in matrix:
    for elemento in row:
        print(elemento)
    #print(row)

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
