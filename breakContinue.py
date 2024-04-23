#ejemplo
print("Ejemplo de break con while")
i = 0
while i < 6:
    i += 1
    if i == 3:
        break
    print(i)

print("\nEjemplo de continue con while")
i = 0
while i < 6:
    i += 1
    if i == 3:
        #print('\nreseteo con i = 3\n')
        continue
    print(i)

