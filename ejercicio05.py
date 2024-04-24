print('Ejercicio05 - Existencia')
fruits = {"manzana":5, "peras":2, "naranjas":4}
print(f'Las frutas son: {fruits}\,')

key = list(fruits.keys())

conocer = input('\nPrimera Forma\nQue fruta quieres conocer? =>')

for i in key:
    if i==conocer:
        print(True)
    else:
        print(False)

#
print('\nSegunda Forma')
if conocer in fruits:
    print(True)
else:
    print(False)