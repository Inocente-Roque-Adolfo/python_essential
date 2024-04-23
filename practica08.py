print('Tabla de multiplicar'.center(50,'-'))
while  True:
    try:
        numero = int(input("¿De que numero quieres la tabla?: "))
        break
    except ValueError:
        print("Solo número entero")

while True:
    try:
        cantidad = int(input("Introduce la cantidad de la tabla: "))
        break
    except ValueError:
        print("Solo número entero")
print('Tabla de multiplicar del',numero)
for indice in range(0, cantidad+1):
    print(numero,'x',indice,'=',numero*indice)
print('Fin del ciclo for')
