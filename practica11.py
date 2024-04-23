lista = ['A', 'B', 'b', 'c', 'E', 'E', 'f']
listaNueva = []
print(f'Lista original: {lista} con {len(lista)} elementos\n')

elim = input('Ingrese el elemento a eliminar: ')

for indice in range(len(lista)):
    if lista[indice].lower() != elim.lower() :
        listaNueva.append(lista[indice])
    
print('Lista final: ', listaNueva)