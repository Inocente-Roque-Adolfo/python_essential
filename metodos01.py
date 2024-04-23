# metodos strip(), lstrip() y rstrip()
cadena = '\t\t=============hola mundo============'
print(cadena)

#borra los espacios en blanco
print(cadena.strip())  
#busca los caracteres de la cadena y los borra si estan en los extremos
print(cadena.strip("= hlo\t"))
#borra los caracteres de ambos lados
print(cadena.strip("="))



#borra los caracteres de la izquierda
print(cadena.lstrip("="))
print(cadena.lstrip("= h \t o"))


#borra los caracteres de la derecha
print(cadena.rstrip("="))
print(cadena.rstrip("= o d"))






