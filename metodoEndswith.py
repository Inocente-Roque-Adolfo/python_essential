#metodo endswith() - retorna True si la cadena termina con el sufijo especificado, de lo contrario False    
cadena = "Hola Mundo"
print(cadena.rjust(20, '*'))
print('Si termina con o minuscula -',cadena,'=>', cadena.endswith('o')) # True
print('No termina con O mayuscula -',cadena,'=>',cadena.endswith('O')) # False

print('\n')
# metodo endswith() - se puede especificar un rango de busqueda
print(cadena.endswith('a', 2)) # false
print(cadena.endswith('o', 1)) # true
print(cadena.endswith('o', 2)) # true
print(cadena.endswith('o', 2, 9)) # false
print(cadena.endswith('d', 2, 9)) # true

