#Mayor y menor edad

#Primera forma con busqueda
personas = (("Eduardo",26),("Maria",30),("Gerardo",20),("Valentina", 22))
print('Tupla personas:'.ljust(15),f'{personas}\n')
edad_menor, edad_mayor = 0, 0

index,index_menor,index_mayor = 0,0,0

for name, edad in personas:
    if edad>=edad_mayor:
        index_menor = index_mayor
        edad_menor = edad_mayor
        edad_mayor = edad
        index_mayor = index
    elif edad<edad_menor:
        edad_menor = edad
        index_menor = index
    index+=1

print(f'La persona de menor edad es: {personas[index_menor]}')
print(f'La persona de mayor edad es: {personas[index_mayor]}')


#Segunda forma con ordenamiento ascendente
#j=1+i
personas_listas = list(personas)

for i in range(len(personas_listas)):
    for j in range(i+1,len(personas_listas)):
        if personas_listas[i][1]>personas_listas[j][1]:
            temporal = personas_listas[i]
            #personas_listas[i], personas_listas[j] = personas_listas[j],temporal
            personas_listas[i] = personas_listas[j]
            personas_listas[j] = temporal

print('\nTupla personas:'.ljust(15),f'{personas_listas}')
print(f'La persona de menor edad es: {personas_listas[0]}')
print(f'La persona de mayor edad es: {personas_listas[-1]}')
