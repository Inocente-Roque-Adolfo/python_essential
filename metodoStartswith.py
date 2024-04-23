#metodo startswith() - retorna True si la cadena comienza con el prefijo especificado, de lo contrario False
cadena = "Hola Mundo"
print(cadena)
print('Si empieza con H-',cadena,'=>', cadena.startswith('H')) # True
print('No empieza con h-',cadena,'=>',cadena.startswith('h')) # False

print('\n')
# metodo startswith() - se puede especificar un rango de busqueda
print(cadena.startswith('M', 5)) # True
print(cadena.startswith('m', 5)) # False
print(cadena.startswith('Mundo', 5, 11)) # True

print('\n')
#con negativos
print(cadena.startswith('o', -1)) # True
print(cadena.startswith('M', -5)) # True