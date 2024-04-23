# clase range
#
# range(inicio, fin, paso)
# inicio: valor inicial del rango
# fin: valor final del rango
# paso: incremento del rango

#un argumento (fin)
#range(fin) = range(0, fin, 1)
rangoUnArgumento = range(10)    # 0<=x<10, x+=1
print(list(rangoUnArgumento))

#dos argumentos (inicio, fin)
#range(inicio, fin) = range(inicio, fin, 1)
rangoDosArgumentos = range(5, 10)   # 5<=x<10, x+=1
print(list(rangoDosArgumentos))

#tres argumentos (inicio, fin, paso)
rangoTresArgumentos = range(0, 10, 2) # 0<=x<10, x+=2
print(list(rangoTresArgumentos))

#rango inverso
rangoInverso = range(10, 0, -1) # 10<=x<0, x-=1
print(list(rangoInverso))

#rango sin secuencia 
rangoInverso = range(10, 0) # 10<=x<0, x+=1
print(list(rangoInverso))
