# metodos lower() islower()

# Metodo lower() convierte una cadena a minusculas

cadena = "Hola Mundo"
print(cadena.islower()) #False
print(cadena.lower()) #hola mundo

cadena = "HOLA MUNDO"
print(cadena.islower()) #False
print(cadena.lower()) #hola mundo'

cadena = "hola mundo"
print(cadena.islower()) #True
print(cadena.lower()) #hola mundo


print("\n")
# metodos upper() isupper()
# isupper() devuelve True si la cadena de texto está en mayúsculas. Si la cadena de texto contiene dígitos o caracteres especiales, el método devuelve False.   
# uper convierte una cadena a mayusculas

cadena = "Hola Mundo"
print(cadena.isupper()) #False
print(cadena.upper()) #HOLA MUNDO

cadena = "HOLA MUNDO"
print(cadena.isupper()) #True
print(cadena.upper()) #HOLA MUNDO

cadena = "hola mundo"
print(cadena.isupper()) #False
print(cadena.upper()) #HOLA MUNDO

print("\n")

# metodos swapcase() isdigit()
# swapcase() convierte las mayúsculas en minúsculas y viceversa.

cadena = "Hola Mundo"
print(cadena.swapcase()) #hOLA mUNDO

cadena = "HOLA MUNDO"
print(cadena.swapcase()) #hola mundo

cadena = "hola mundo"
print(cadena.swapcase()) #HOLA MUNDO

print("\n")
#metodo capitalize()
# capitalize() convierte la primera letra de la cadena en mayúscula y el resto en minúsculas.
cadena = "hola mundo"
print(cadena.capitalize()) #Hola mundo

cadena = "HOLA MUNDO"
print(cadena.capitalize()) #Hola mundo

cadena = "el VIAJE eS la RecompEnsa"
print(cadena.capitalize()) #El viaje es la recompensa\

