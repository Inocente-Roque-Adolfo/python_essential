#find 

frase = input("Digite uma frase: ")
palabra = input("Digite uma palabra a borrar: ")

posicion_palabra_inicio = frase.find(palabra)
posicion_palabra_final = posicion_palabra_inicio + len(palabra)

cadena_nueva = frase[:posicion_palabra_inicio] + frase[posicion_palabra_final:]

print(cadena_nueva)



