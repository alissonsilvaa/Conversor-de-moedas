# Valida um número inteiro e positivo
while True:
    try:
        n = int(input("Digite um numero inteiro e positivo:"))
        if n <= 0:
            raise TypeError
    except ValueError:
        print("ERRO - O numero deve ser inteiro.")
    except TypeError:
        print("ERRO - O numero deve ser positivo")
    except Exception as erro:
        print(type(erro))    # imprime o tipo do erro generico que foi gerado
    else:
        break


print("Continua a executar o resto do programa.......")
