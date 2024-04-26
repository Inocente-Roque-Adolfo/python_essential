#Suma de elementos Tuplas
tuple1 = (1,2,3,4,5)
tuple2 = (8,6,4,2,0)
suma_tuplas = []


for index in range(len(tuple1)):
    suma_tuplas.append(tuple1[index]+tuple2[index])
suma_tuplas = tuple(suma_tuplas)

print(f'Tuple 1:     {tuple1}\n             +\nTuple 2:     {tuple2}\n             ===============\nSuma:        {suma_tuplas}')

#Segunda forma
add =[]
for x, y in zip(tuple1, tuple2):
    add.append(x+y)
#print('resultado'.ljust(15), add)
print(f'\n\nTuple 1:     {tuple1}\n             +\nTuple 2:     {tuple2}\n             ===============\nSuma:        {tuple(add)}')



