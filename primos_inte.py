import math

def primos_ate_n(n):
    if  n <= 1:
        return None

    lista = []
    for num in range(2, n + 1):
        eh_primo = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            lista.append(num)

    return lista


n = int(input("Digite um numero N (N > 1): "))

resultado = primos_ate_n(n)

if resultado is not None:
    print(f"Numeros primos ate {n}: {resultado}")
else:
    print("N precisa ser um numero maior que 1")