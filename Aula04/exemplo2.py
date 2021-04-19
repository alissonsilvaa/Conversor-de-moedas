# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.
# Solicitar os dados novamente caso o usuário informar valores inválidos

while True:
    try:
        a = int(input('Informe um número inteiro positivo: '))
        b = int(input('Informe um número inteiro positivo: '))
        c = a / b
        print('Resultado da divisão: ', c)
    except ZeroDivisionError:
        print("Divisao por zero")
    except ValueError:
        print("O numero deve ser inteiro")
    except Exception:
        print("Erro inesperado")
    else:               # executa quando não há erro
        print("Operacao realizada com sucesso")
        break
