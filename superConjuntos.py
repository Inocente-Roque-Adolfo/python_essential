conjuntoA = {1,2,3,4,5}
conjuntoB = {2,5}
conjuntoC = {2,6}
print(f'conjuntoA: {conjuntoA}\nconjuntoB: {conjuntoB}\nconjuntoC: {conjuntoC}')

#¿Conjunto A es superconjunto de B? #dentro de A esta B ?
print('Dentro de A esta B: ',conjuntoA.issuperset(conjuntoB))
print('Dentro de A no esta C: ',conjuntoA.issuperset(conjuntoC))

set_inclusivo_b_a = conjuntoA>=conjuntoB
print('(A>=B)   A es superconjunto de B: ',set_inclusivo_b_a)

set_estricto = conjuntoC>conjuntoB
print('(C>B)   C no es superconjunto de B: ',set_estricto)
