def primos(n, i=2):
    if n <= 1:
        return None
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return primos(n, i + 1)


def primos_ate_n(n, atual=2):
    if n <= 1:
        return None
    if atual > n:
        return []

    if primos(atual):
        return [atual] + primos_ate_n(n, atual + 1)
    else:
        return primos_ate_n(n, atual + 1)


n = int(input("Digite um numero N (N > 1): "))

resultado = primos_ate_n(n)

if resultado is not None:
    print(f"Numeros primos ate {n}: {resultado}")
else:
    print("N precisa ser um numero maior que 1")