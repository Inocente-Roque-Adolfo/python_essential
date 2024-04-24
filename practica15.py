# Contar la cantidad de letras del string y guardar en un diccionario
#Primera forma
string = input('Ingresa un texto: ')
diccionario = {}
for letra in list(string):
    counter = 1
    if letra in diccionario.keys():
        valor = diccionario[letra]
        counter = valor+1
    diccionario.update({letra: counter})
print(diccionario,'\n')

#Segunda forma
letters = dict.fromkeys(string, 0)
for letras in string:
    letters[letras]+=1
print(letters,'\n')

