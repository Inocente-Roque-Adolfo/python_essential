print('\nSISTEMA DE VACACIONES\n')
nombre = input('Ingrese su nombre: ')
clave = int(input('Ingrese su clave (1-3): '))
antiguedad = float(input('Ingrese su antigüedad: '))
print('=====================================')
print('\nUsuario: ', nombre)
if clave == 1:
    print('Departamento: Atencion al cliente\n')
    if antiguedad == 1:
        print(f'{nombre} tiene derecho a 6 días de vacaciones')
    elif antiguedad >= 2 and antiguedad <= 6:
        print(f'{nombre} tiene derecho a 14 días de vacaciones')
    elif antiguedad >= 7:
        print(f'{nombre} tiene derecho a 20 días de vacaciones')
    else:
        print('Error en la antigüedad')
elif clave == 2:
    print('Departamento: Logistica\n')
    if antiguedad == 1:
        print(f'{nombre} tiene derecho a 7 días de vacaciones')
    elif antiguedad >= 2 and antiguedad <= 6:
        print(f'{nombre} tiene derecho a 15 días de vacaciones')
    elif antiguedad >= 7:
        print(f'{nombre} tiene derecho a 22 días de vacaciones')
    else:
        print('Error en la antigüedad')
elif clave == 3:
    print('Departamento: Gerencia\n')
    if antiguedad == 1:
        print(f'{nombre} tiene derecho a 10 días de vacaciones')
    elif antiguedad >= 2 and antiguedad <= 6:
        print(f'{nombre} tiene derecho a 20 días de vacaciones')
    elif antiguedad >= 7:
        print(f'{nombre} tiene derecho a 30 días de vacaciones')
    else:
        print('Error en la antigüedad')
else:
    print('\nError en la clave')
print('\nFin del programa\n')


