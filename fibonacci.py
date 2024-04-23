print('\nserie de fibonacci\n')
limite, respuesta = 1597, 0
primer_digito_sumante, segundo_digito_sumante = 0, 1

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