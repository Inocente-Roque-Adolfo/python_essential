print('Sistema para calcular el promedio de notas')
nombre = str(input('Para comenzar, ¿Cuál es tu nombre? '))
while not nombre.isalpha():
    print('Error. Ingresa solo letras.')
    nombre = str(input('Para comenzar, ¿Cuál es tu nombre? '))


while True:
    try:
        nota1 = float(input(nombre + ' Ingrese la primera nota: '))
        while not 0 <= nota1 <= 20:
            print('Error. Ingresa un número entre 0 y 20.')
            nota1 = float(input(nombre + ' Ingrese la primera nota: '))
        break
    except ValueError:
        print("Error. Ingresa solo números.")

while True:
    try:
        nota2 = float(input(nombre + ' Ingrese la segunda nota: '))
        while not 0 <= nota2 <= 20:
            print('Error. Ingresa un número entre 0 y 20.')
            nota2 = float(input(nombre + ' Ingrese la segunda nota: '))
        break
    except ValueError:
        print("Error. Ingresa solo números.")

while True:
    try:
        nota3 = float(input(nombre + ' Ingrese la tercera nota: '))
        while not 0 <= nota3 <= 20:
            print('Error. Ingresa un número entre 0 y 20.')
            nota3 = float(input(nombre + ' Ingrese la tercera nota: '))
        break
    except ValueError:
        print("Error. Ingresa solo números.")

promedio = (nota1 + nota2 + nota3) / 3
promedio = round(promedio, 2)

if promedio >= 10.5:
    print('Felicidades', nombre, '"has aprobado" con un promedio de:', promedio)
else:
    print('Lo siento', nombre, 'has reprobado con un promedio de:', promedio)    


