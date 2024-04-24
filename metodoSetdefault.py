# metodo Setdefault()

# setdefault() es un método que devuelve el valor de una clave 
#             (si la clave está en el diccionario). 
#              Si no está, inserta la clave con el valor predeterminado que le proporcionamos.

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(diccionario,'\n')

# Ejemplo de uso de setdefault()
item = diccionario.setdefault('a')
print(item)  # 1
print(diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


item = diccionario.setdefault('z', 100)
print(item)  # 100
print(diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'z': 100}

item = diccionario.setdefault('x')
print(item)
print(diccionario,'\n')  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'z': 100, 'x': None}