
'''Escreva uma função que conta a quantidade de vogais em um 
texto e armazena tal quantidade em um dicionário, onde 
a chave é a vogal considerada e o valor é a quantidade de 
vezes que essa vogal aparece no texto. A função deve 
receber o texto como entrada, e retornar o dicionário.
'''


def conta_vogais(texto):
    dicionario = {}
    texto = texto.lower()        # converte texto para minusculo

    for c in texto:            # percorre os caracteres da string
        vogais = 'aeiou'
        if c in vogais:        # verifica se caracter é uma vogal
            if c in dicionario:
                # executa quando a vogal ja existe no dicionario
                dicionario[c] += 1
            else:
                # executa apenas quando a vogal ainda nao
                dicionario[c] = 1
    return dicionario


# Programa principal
texto = 'faculdade de tecnologia impacta'
dicionario = conta_vogais(texto)                   # chama a função
print(dicionario)
