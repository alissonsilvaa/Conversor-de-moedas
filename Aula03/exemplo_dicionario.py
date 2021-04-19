# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {12345678: "Paulo", 88888888: "Maria", 4565456: "João"}

print(cadastro)
print(cadastro[12345678])   # Paulo

# Adicionar os dados de uma pessoa no dicionario
cadastro[999999999] = 'João'
print(cadastro)

# Alterar o Nome de uma pessoa
cadastro[999999999] = 'João Pedro'
print(cadastro)

# Excluir os dados de uma pessoa
cadastro.pop(88888888)
print(cadastro)

# Verificar se chave existe no dicionário
if 999999999 in cadastro:
    print('Existe')
else:
    print('Não existe')

# Percorrer o dicionario
for a in cadastro:
    print(a, cadastro[a])

'''
# preencher dicionário com dados informados pelo usuário
cadastro = {}
for i in range(3):
    cpf = int(input('CPF:'))
    nome = input('Nome:')
    cadastro[cpf] = nome
print(cadastro)
'''

# exemplo de função
def busca(dicionario, cpf):
    if cpf in dicionario:
        return dicionario[cpf]

print(busca(cadastro, 123456))


# EXEMPLO 2:
# Dicionario para armazenar o nome de um aluno e uma lista com 5 notas
alunos = {"Paulo": [9, 8, 7, 4, 10],
          "Maria": [8, 3, 8, 9, 10],
          "Pedro": [10, 7, 6, 4, 8]}

# Exibir lista de notas de um aluno
print(alunos["Pedro"])

# Inserir uma nova nota para um aluno
alunos["Pedro"].append(9)
print(alunos)


# exemplo de dicionario dentro de outro dicionario
notas = {123456: {"Banco de Dados": [8, 9, 6, 10, 5],
                  "Programação": [6, 7, 8, 4, 9]},
         789456: {"Banco de Dados": [8, 9, 5, 5, 5],
                  "Programação": [6, 7, 3, 6, 9]}}
