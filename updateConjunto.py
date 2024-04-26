#Agregar varios elementos al conjunto
# metodo update()
""""
solo permite un argumento
pero el argumto debe ser un objeto iterable

los conjuntos no permiten que se repita un elemento
"""

colores = {"verde","rojo","azul"}
nuevos_colores = ["amarillo", "morado","azul"]
print('Colores: ',colores,'\nNuevos colores: ',nuevos_colores)

colores.update(nuevos_colores)
print('Nuevos colores agregados: ',colores)