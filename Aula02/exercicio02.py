'''
Preencha uma lista com 10 números digitados pelo usuário.
A partir desta lista, gere uma lista com os números pares
e outra com os números ímpares.
'''

lista = []
for a in range(10):
    n = int(input('Numero: '))
    lista.append(n)

print(lista)

pares = []
impares = []
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(pares)
print(impares)
