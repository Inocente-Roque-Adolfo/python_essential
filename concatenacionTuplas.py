#Concatenacion tuplas
#Operador + , con ese orden se concatenan las tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla3) # (1, 2, 3, 4, 5, 6)

#Operador +=
tupla2 += tupla1
print(tupla2) # (4, 5, 6, 1, 2, 3)

#Operador += #en listas
list1 = [1,2,3]
list2 = [4,5,6]
list2 += list1
print(list2) # [4, 5, 6, 1, 2, 3]

#Operador *
tupla4 = tupla1 * 3
print(tupla4) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

#Funcion tuple
tupla5 = tuple([1,2,3])
tupla6 = tuple([4,5,6])
tupla7 = tupla5 + tupla6
print(tupla7) # (1, 2, 3, 4, 5, 6)

