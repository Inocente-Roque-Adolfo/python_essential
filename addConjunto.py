#Agregar un elemento al conjunto
# metodo add()
""""
solo permite un argumento
"""
frutas = {"manzana", "pera", "uva"}
print('Conjunto original: ',frutas)

frutas.add("pera") 
print('Intente agregar pera: ',frutas)

frutas.add("naranja") 
print('Agregue naranja: ',frutas)

tuplas = ("mangos","sandia")
frutas.add(tuplas)
print('Agregue una tupla: ',frutas)