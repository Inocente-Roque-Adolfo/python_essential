#metodo istitle() devuelve True si la cadena de texto comienza con una letra mayúscula y el resto de las letras son minúsculas. 
#Si la cadena de texto contiene dígitos o caracteres especiales, el método devuelve False.
cadena = "Hola"
print(cadena.istitle()) #True

cadena = "hola"
print(cadena.istitle()) #False
print(cadena,'=>',cadena.title()) #Hola

cadena = "Hola Mundo"
print(cadena.istitle()) #True

cadena = "Hola MundO"
print(cadena.istitle()) #False
print(cadena,'=>',cadena.title()) #Hola Mundo

cadena = "Hola mundo"
print(cadena.istitle()) #False
print(cadena,'=>',cadena.title()) #Hola Mundo


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombreCompleto = nombre + " " + apellido
if not nombreCompleto.istitle():
    print("\nNombre completo inválido: ", nombreCompleto)
    nombreCompleto = nombreCompleto.title()
    print("Nombre completo corregido: ", nombreCompleto)

print("\nNombre completo: ", nombreCompleto)