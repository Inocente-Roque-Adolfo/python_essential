print('Ejercicio01 - Frutas')

fruits = {"manzana":5, "peras":2, "naranjas":4}

conocer = input("Que fruta quieres conocer: ")

dato = fruits.get(conocer)
#dato2 = fruits[conocer]

if dato!=None:
    #print(f'Hay {dato} de {conocer}')
    #print(f'Hay {dato2} de {conocer}')

    for key, values in fruits.items():
        if key==conocer:
            print(f'Hay {values} de {conocer}')
else:
    respuesta = input('No existe esa fruta\n¿Quieres agregar una cantidad yes/no? =>').lower()
    if respuesta=='yes' or respuesta=='si':
        cantidad = int(input(f'Ingrese la cantidad de {conocer}: '))
        fruits.setdefault(conocer, cantidad)
        for key, values in fruits.items():
            if key==conocer:
                print(f'Hay {values} de {conocer}')
        seguir = input('quieres seguir agregando?')
        #if seguir.lower=='yes' or seguir.lower=='si':
        while not seguir.lower=='yes':
            nuevaFruta = input('Cual es la fruta: ')
            nuevaCantidad = input('Cual es la cantidad: ')
            fruits.update([(nuevaFruta,nuevaCantidad)])
            fruits.get(nuevaFruta)
            print(f'Hay {fruits.get(nuevaFruta)} de {nuevaFruta}')
            seguir = input('quieres seguir agregando?')
            if seguir.lower!='yes' or seguir.lower!='si':
                break
                
        print('Las frutas que hay son: ', end='')
        for clave in fruits.keys():
            print(clave, end='-')
    else:
        print('adios...')




