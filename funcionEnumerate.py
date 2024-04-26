#Funcion enumerate
# enumerate(objeto_iterable) .... por defecto el star = 0
# enumerate(objeto_iterable, star=0)
"""
Secuencia q lleva la posicion
retorna primero la POSICION y luego el ELEMENTO
"""

frutas = ["manza",'platanos','úva','sandia']
print(frutas)

for posicion, elemento in enumerate(frutas):
    print(f'En la posicion {posicion} esta {elemento}')

print('\nEmpezando desde 101')
for posicion, elemento in enumerate(frutas,start=101):
    print(f'En la posicion {posicion} esta {elemento}')

print('\nGuardar en una lista de tuplas')
enumerado = list(enumerate(frutas,start=1))
print(enumerado)