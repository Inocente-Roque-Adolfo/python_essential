list = [1,2,3,4,5]
list_copy = list.copy()
print(list_copy)

#fromkeys()
# Path: metodoFromkeys.py
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)

#key son diccionarios
# Path: metodoFromkeys.py
keys = {'a': {'apple':1}, 'b': {'banana':2}, 'c': {'cherry':3}}
vowels = {}.fromkeys(keys,keys)
print(vowels)

#un argumento fromkeys()
# Path: metodoFromkeys.py
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = {}.fromkeys(keys)
print(vowels)


