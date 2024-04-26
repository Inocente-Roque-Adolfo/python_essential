#Interseccion entre conjuntos
#metodo: intersection() or &

""""
Encuentra elelmentos en comun entre los conjuntos
"""

conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8}
conjuntoC = {8,9,10}
print(f'conjuntoA: {conjuntoA}\nconjuntoB: {conjuntoB}\nconjuntoC: {conjuntoC}\n')

conjunto_A_B = conjuntoA.intersection(conjuntoB)
print('Interseccion entre A y B: ',conjunto_A_B)
# con operador &
conjunto_A_B = conjuntoA&conjuntoB
print('Interseccion entre A y B con (&): ',conjunto_A_B)

#si no tienen nada en comun
conjunto_A_C = conjuntoA.intersection(conjuntoC) # REGRESA CONJUNTO VACIO
print('Interseccion entre A y C: ',conjunto_A_C)   # set()
