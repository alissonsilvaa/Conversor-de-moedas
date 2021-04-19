'''
Preencha uma lista com 10 números digitados pelo usuário e exiba:
a - o maior número da lista
b - o menor número da lista
c - a quantidade de números pares contidos na lista
d - a média dos números contidos na lista
e - todos os números menores do que a média calculada no item anterior
'''

lista = []
for a in range(10):
    n = int(input("Informe um numero inteiro: "))
    lista.append(n)
    
print(lista)

maior = max(lista)
print('Maior:', maior)

menor = min(lista)
print('Menor:', menor)

contador = 0
for a in lista:
    if a % 2 == 0:
        contador += 1
print('Quantidade de pares:', contador)

media = sum(lista) / len(lista)
print('Média:', media)

print('Numeros menores que a média:')
for a in lista:
    if a < media:
        print(a)

# exemplo utilizando while
contador = 0
a = 0
while a < len(lista):
    if lista[a] % 2 == 0:
        contador += 1
    a += 1
print('Quantidade de pares:', contador)
