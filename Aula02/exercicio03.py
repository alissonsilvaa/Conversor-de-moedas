'''
Preencha duas tuplas com 5 números cada, informados pelo usuário.
Concatene as duas tuplas e exiba a tupla resultante.
'''

lista1 = []
lista2 = []

for a in range(5):
    n = int(input('Numero:'))
    lista1.append(n)
print(lista1)

for a in range(5):
    n = int(input('Numero:'))
    lista2.append(n)
print(lista2)

tupla1 = tuple(lista1)      # tuple: converte uma lista para tupla
tupla2 = tuple(lista2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
