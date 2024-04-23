numeros = [0,1,2,3,4,5,6,7]
eliminados = []
print('Lista original: ',numeros)
eliminados.append(numeros[0])
numeros.pop(0) #elimina el primer elemento

eliminados.append(numeros[-1])
numeros.pop(-1) #elimina el ultimo elemento o numeros.pop()
print('Lista eliminado: ',numeros)
print('Elementos eliminados: ',eliminados)