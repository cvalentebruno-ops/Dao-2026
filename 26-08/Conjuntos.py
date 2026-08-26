import random

"""
todos = [random.randint (1,20 ) for i in range (10) ]
numeros = set(todos)

print(numeros)
print(len(numeros))
print(todos)
"""

clientes = { 2:"juan", 32:"Ana", 15:"Luis"}
if 2 in clientes:
    print("existe")

for x in clientes.keys ():
    print(clientes[x])