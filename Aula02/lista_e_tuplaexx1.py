'''
Preencha uma lista com 10 números digitados pelo usuário e exiba:
o maior número da lista
o menor número da lista
a quantidade de números pares contidos na lista
a média dos números contidos na lista
todos os números menores do que a média calculada no item anterior
'''
lista = []
for a in range(10):
    n = int(input('Informe um número inteiro: '))
    lista.append(n)