try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
except ZeroDivisionError:
    print("Ocorreu uma divisao por zero")
except ValueError:
    print("O tipo de dado é invalido")
except Exception:
    print("Erro inesperado")
