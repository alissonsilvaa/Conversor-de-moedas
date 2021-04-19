produtos = {}

for i in range(5):
    nome = input('Nome do produto:')
    preco = float(input('Preço do Produto:'))
    if nome in produtos:
        print("Produto ja existe")
    else:
        produtos[nome] = preco
print(produtos)

for i in produtos:
    if produtos[i] > 50:
        print(i, '-', produtos[i])
