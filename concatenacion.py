#concatenacion

mensaje = 'hola'

espacio = ' '

nombre = 'mundo'

print(mensaje + espacio + nombre)

numero = 5
numero = str(numero)

#print(mensaje + espacio + nombre + espacio + str(numero))
print(mensaje + espacio + nombre + espacio + numero)

# forma de concatenar con format
print('Hola {}'.format('mundo'))

# concatenar con format y variables
nombres = 'Juan'
edad = 22
print('Hola {} tienes {} años'.format(nombres,edad))
print("Hola {1} tienes {0} años" .format(nombres,edad))
print(f'hola {nombres} tienes {edad} años')
print(f'{4+5}')

nombre = input('Cual es tu nombre? ')
numero = int(input('Ingresa un numero: '))
print(f'Hola {nombre} el numero que ingresaste es {numero}')

