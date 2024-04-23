dict_name = {'a':1, 'b':2, 'c':3}
print(dict_name)

print(dict_name.get('a')) # 1
print(dict_name.get('d')) # None

print(dict_name.get('d', 'No existe')) # No existe


noExiste = dict_name.get('d')

if noExiste:
    print('Existe')
