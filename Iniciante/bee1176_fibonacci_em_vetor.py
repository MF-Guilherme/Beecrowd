def fibonacci(indice):
    lista = [0, 1]

    for i in range(62 - 2):
        add = lista[-1] + lista[-2]
        lista.append(add)
    valor = lista[indice]
    return valor

t = int(input())

for i in range(t):
    n = int(input())
    print(f'Fib({n}) = {fibonacci(n)}')