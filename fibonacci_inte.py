def fibonacci(n):
    if n == 1 or n == 0:
        return n
    elif n < 0:
        print("esse programa nao calcula fibonacci de numeros negativos")
    else:
        anterior = 0
        atual = 1
        for i in range(2, n + 1):
            novo_atual = anterior + atual
            anterior = atual
            atual = novo_atual

    return atual

n = int((input("digite n para sabe o valor de fibonacci:")))
print(fibonacci(n))