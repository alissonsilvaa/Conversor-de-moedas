def eh_perfeito(n):         # n = 28
    if n == 0:              # zero não é perfeito
        return False

    soma = 0
    for i in range(1, n):   # 1...27
        if n % i == 0:
            soma += i       # soma os divisores

    if soma == n:           # verifica se é perfeito
        return True
    else:
        return False
