#Union de Conjuntos
#metodo: union() or |

conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8}
conjuntoC = {8,9,10}
print(f'conjuntoA: {conjuntoA}\nconjuntoB: {conjuntoB}\nconjuntoC: {conjuntoC}\n')


conjunto_A_B = conjuntoA.union(conjuntoB)
print('Union entre A y B: ',conjunto_A_B)

conjunto_A_C = conjuntoA.union(conjuntoC)
print('Union entre A y C: ',conjunto_A_C)

conjunto_B_C = conjuntoB|conjuntoC
print('Union entre B y C con el operador(|): ',conjunto_B_C)
