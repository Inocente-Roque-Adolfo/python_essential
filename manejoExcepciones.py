#Manejo de excepciones
try:
    numero = int(input('Ingresa un numero: '))
except ValueError as ve:
    print(f'error tipo ValueError: {ve}')
try:
    division = 50/numero

except NameError:
    print('error tipo NameError')
except ZeroDivisionError as zde:
    print(f'error tipo ZeroDivisionError: {zde}')


try:
    print(f'La division entre 50/{numero} =',division)
except Exception as e:
    print(f'error tipo Exception as e: {e}')

else:
    print(f'Satisfactorio sin excepciones')
finally:
    numero = 0
    print(f'Terminado')

print(numero)

