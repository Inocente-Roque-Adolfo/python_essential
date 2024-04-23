#not 
numero = 5

if not numero == 5:
    print ("El número es diferente de 5")
else :
    print ("El número es igual a 5")

#conjucion 
num1 = int(input("\nIntroduce un número: "))
if num1 > 0 and num1 < 10:
    print("El número",num1,"es mayor que 0 y menor que 10")
else:
    print("El número",num1,"no cumple con la condición")

#disyuncion
num2 = int(input("\nIntroduce un número: "))
if num2 < 0 or num2 > 10:
    print("El número",num2,"es menor que 0 o mayor que 10")
else:
    print("El número",num2,"no cumple con la condición")

