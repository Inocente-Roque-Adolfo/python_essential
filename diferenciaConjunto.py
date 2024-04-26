#Diferencia Conjunto
# metodo: difference()
"""
Tiene orden
A.difference(B)
de A se obtiene la diferencia
de B solo se compara
Retorna lo que esta en el conjunto A(lado izquierdo) y no esta en B (lado derecho)
"""

conjuntoA = {1,2,3,4,5}
conjuntoB = {4,5,6}
conjuntoC = {4,5,6}
print(f'conjuntoA: {conjuntoA}\nconjuntoB: {conjuntoB}\nconjuntoC: {conjuntoC}\n')

diferencia_A_B = conjuntoA.difference(conjuntoB)
print('Diferencia de A con B:',diferencia_A_B)

diferencia_B_A = conjuntoB.difference(conjuntoA)
print('Diferencia de B con A:',diferencia_B_A)

diferencia_A_B = conjuntoA-conjuntoB
print('Elementos de A pero no de B:',diferencia_A_B)

diferencia_B_A = conjuntoB-conjuntoA
print('Elementos de B pero no de A:',diferencia_B_A)

#conjuntos iguales
diferencia_B_C = conjuntoB-conjuntoC        #RETORNA UN CONJUNTO VACIO
print('Diferencia entre conjuntos iguales:',diferencia_B_C) #set()