# LISTAS:

# Sequencias de elementos. 
# Delimitada por colchetes [ ]
a = [3, 6, 8]


# Listas heterogêneas: Pode conter diferentes tipos de dados 
b = [2, 'abc', 4.5]

# listas vazias
c = []

# função print pode ser utilizada para exibir os itens contidos na lista
lista = [2, 5, 6]
print(lista)

# Índice: especifica a posição de um item na lista
# Índice inicial é 0
print(lista[0])

# Índices negativos indicam posições referente ao final da lista
print(lista[-1])

# append: adiciona item ao final da lista
lista.append(100)
print(lista)

# repetição for para percorrer a lista
for a in lista:
    if a % 2 != 0:
        print(a)

# preencher lista com dados informados pelo usuário
lista = []
for a in range(5):
    i = int(input('numero:'))
    lista.append(i)
print(lista)


# ---------------------------------------------------
# PRINCIPAIS FUNÇÕES

lista = [3, 5, 7, 8, 5, 9, 8, 10]

# len: Retorna o tamanho de uma lista
print(len(lista))

# count: Contar quantas vezes um item aparece na lista
print(lista.count(5))

# index: Retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
# in: verificar se determinado item existe em uma lista
if 5 in lista:
    print(lista.index(5))
else:
    print('Item não encontrado')


# insert: insere item em determinada posição
lista.insert(3, 200)
print(lista)

# pop: Remove o último item da lista
lista.pop()
print(lista)

# pop: Remove um item pelo indice
lista.pop(0)
print(lista)

# remove: Remove primeira ocorrencia de um item da lista
lista.remove(5)
print(lista)

# remover varios itens da lista
while 5 in lista:
    lista.remove(5)
print(lista)

# sort: ordenação da lista
lista.sort()
print(lista)

# ordenação decrescente
lista.sort(reverse=True)
print(lista)

# min: menor elemento
print(min(lista))

# max: maior elemento
print(max(lista))

# sum: somatorio da lista
print(sum(lista))

# media
print(sum(lista) / len(lista))

# concatenação de listas
lista1 = [4,7,8]
lista2 = [3,4]
lista3 = lista1 + lista2
print(lista3)


# ----------------------------------------------
# TUPLAS

# Sequencias de elementos que não podem ser alteradas
# Delimitada por parenteses ( )
tupla = (4, 7, 8)

# tuplas vazias
tuplavazia = ()


# tuplas de 1 elemento (tem uma virgula no final)
tupla = (10,)
print(tupla)

# acesso pelo índice
tupla = (4, 6, 7, 8)
print(tupla[1])

# repetição for pode ser utilizada para percorrer a tupla
for a in tupla:
    print(a)

# concatenção de tuplas
tupla1 = (3,5,6)
tupla2 = (5,7,8)
tupla3 = tupla1 + tupla2
print(tupla3)
