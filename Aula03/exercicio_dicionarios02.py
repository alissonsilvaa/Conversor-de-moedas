'''Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário
Percorra o dicionário e exiba a média de cada aluno.
'''

alunos = {}

for i in range(5):                 #quantidade de alunos
    ra = input('Informe o RA: ')
    n1 = float(input('informe a Nota 1: '))
    n2 = float(input('Informe a Nota 2: '))
    n3 = float(input('Informe a Nota 3: '))
    lista = [n1, n2, n3]
    alunos[ra] = lista             # inserindo os dados no dicionario

print(alunos)

for ra in alunos:                 # percorre o dicionario
    media = sum(alunos[ra]) / len(alunos[ra])      # calcula a media de cada aluno
    print(media)