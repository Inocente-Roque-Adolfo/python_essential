#Diferencia simetrica
# metodo: symmetric_difference() or ^
"""
No importa el orden
solo retorna los elemtos propios de cada conjunto
No retorna los elementos en comun 
"""
conjuntoA = {1,2,3,4,5}
conjuntoB = {4,5,6}
conjuntoC = {4,5,6}
print(f'conjuntoA: {conjuntoA}\nconjuntoB: {conjuntoB}\nconjuntoC: {conjuntoC}\n')

diferencia_simetrica_A_B = conjuntoA.symmetric_difference(conjuntoB)
print('Diferencia simetrica de A y B:',diferencia_simetrica_A_B)

diferencia_simetrica_B_A = conjuntoB ^ conjuntoA
print('Diferencia simetrica de B y A con (^):',diferencia_simetrica_B_A)