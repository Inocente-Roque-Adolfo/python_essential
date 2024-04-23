#ciclos
numero = 5

while not numero==-2:
    print(numero)
    numero = numero - 1
print('fin del ciclo\n')

while True:
    print('hola\n')
    break

x = 1
while x<50:
    print(x)
    x += x + 1
print('fin del ciclo\n')

#multiplos de 3 ascedente hasta el 50 3, 6, 9, 15, 21, 27, 33, 39, 45
x = 1
while x<50:
    if x%3 == 0:
        print(x)
    x += 1
print('fin del ciclo\n')

#multiplos de 3 descendente hasta el 50 48, 45, 39, 33, 27, 21, 15, 9, 6, 3
x = 50
while x>0:
    if x%3 == 0:
        print(x)
    x -= 1
print('fin del ciclo\n')


#
print('\nserie de fibonacci\n')
limite = 1597
respuesta = 0
primer_digito_sumante=0
segundo_digito_sumante=1

print(primer_digito_sumante,segundo_digito_sumante, sep=' ', end=' ')


while respuesta<limite:
    respuesta = primer_digito_sumante + segundo_digito_sumante
    # 1 = 0 + 1
    # 2 = 1 + 1
    # 3 = 1 + 2
    print(respuesta, end=' ')
    #1
    #2

    almacenamiento_temporal = segundo_digito_sumante
    #1 = 1
    #1 = 1
    segundo_digito_sumante = respuesta
    #1 = 1
    #2 = 2
    primer_digito_sumante = almacenamiento_temporal
    #1 = 1
    #1 = 1
    
    
    
    
    


