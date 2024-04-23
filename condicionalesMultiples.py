while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Por favor, ingrese una edad válida.")


if edad>=60:
    print("Usted es un adulto mayor")
elif edad>=18:
    print("Usted es un adulto")
elif edad>=13:
    print("Usted es un adolescente")
elif edad>=3:
    print("Usted es un niño")
else:
    print("Usted es un bebé")