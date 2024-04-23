frase = input("Introduce una frase: ")
letraTerminal = input("Introduce una letra terminal: ")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for indice in range(0, len(frase)):
    if frase[indice] == letraTerminal:
        break
    elif frase[indice] in vocales:
        print('_', end='')
        continue
    
    print(frase[indice], end='')


    
    