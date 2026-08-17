from functools import lru_cache 

@lru_cache(maxsize=None)


def fibonacci(n):
    if n == 1 or n == 0:
        return n
    elif n < 0:
        print("esse programa nao calcula fibonacci de numeros negativos")
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int((input("digite n para sabe o valor de fibonacci:")))
print(fibonacci(n))