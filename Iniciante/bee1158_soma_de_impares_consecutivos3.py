def soma_de_impares(x, y):
    contador = 0
    lista = []
    while contador < y:
        if not x % 2 == 0:
            lista.append(x)
            contador += 1
        x += 1
    return(sum(lista))

n = int(input())

for i in range(n):
    x, y = map(int, input().split(' '))
    print(soma_de_impares(x, y))