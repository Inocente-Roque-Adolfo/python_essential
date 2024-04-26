conjunto_a= {1,2,3,4,5}
conjunto_b = {2,4}

print(f'conjunto_a: {conjunto_a}\nconjunto_b: {conjunto_b}')
#¿Conjunto B es subconjunto de A? = si 
b_en_a= conjunto_b.issubset(conjunto_a)
print('b esta en a: ',b_en_a)

a_en_b = conjunto_a.issubset(conjunto_b)
print('a no esta en b: ',a_en_b)

#subconjunto inclusivo
""""
operador: <=
si son iguales devuelve true
"""
print(f'\nconjunto_a: {conjunto_a}\nconjunto_b: {conjunto_b}')
set_inclusivo_b_a = conjunto_b<=conjunto_a
print('(conjunto_b<=conjunto_a)b esta en a: ',set_inclusivo_b_a)

set_inclusivo_a_b = conjunto_a<=conjunto_b
print('(conjunto_a<=conjunto_b) a no esta en b: ',set_inclusivo_a_b)


#subconjunto estricto
"""
operador : <
si ambos conjuntos son iguales retorna false 
"""
conjunto_a = {1,2,3,4,5}
conjunto_b = {1,2,3,4,5}
conjunto_c = {2,3,5}
print(f'\nconjunto_a: {conjunto_a}\nconjunto_b: {conjunto_b}\nconjunto_c: {conjunto_c}')
set_estricto = conjunto_a<conjunto_b
print('Son iguales a<b:',set_estricto)
set_estricto = conjunto_b<conjunto_a
print('Son iguales: b<a',set_estricto)
set_estricto = conjunto_c<conjunto_b
print('el conjunto C esta en B: c<b',set_estricto)
