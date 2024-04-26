#Recorrer un conjunto
conjunto = {1,2,3,4,5,6,7,8,9,10}

#recorrer con for
print('Recorriendo con ciclo For')
for elemento in conjunto:
    print(elemento, end=' ')

#recorrer con bucle while
print('\n\nRecorriendo con ciclo While')
lista = list(conjunto)
index = 0
while index<len(lista):
    print(lista[index], end=' ')
    index+=1