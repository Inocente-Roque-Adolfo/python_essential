nombre = input("¿Cuál es tu nombre? ")
#explica por qué se usa isalpha() en la siguiente línea
#isalpha() es un método que devuelve True si todos los caracteres de la cadena son letras, de lo contrario, devuelve False.
while not nombre.isalpha():
    print("Error. Ingresa solo letras.")
    nombre = input("¿Cuál es tu nombre? ")



while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        break
    except ValueError:
        print("Error. Ingresa solo números enteros.")

print("Hola", nombre, "tienes", edad, "años.")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")




print("Hola", nombre, "tienes", edad, "años.")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
