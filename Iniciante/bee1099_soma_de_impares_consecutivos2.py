def soma_impares(n1, n2):
    lista = []
    for j in range(n1, n2+1):
        lista.append(j)
    del(lista[0])
    del(lista[-1])
    if len(lista) == 0:
        print(0)
    else:
        impares = []
        for item in lista:
            if item % 2 != 0:
                impares.append(item)
        print(sum(impares))

testes = int(input())

for i in range(testes):
    x, y = map(int, input().split(' '))
    if x == y:
        print(0)
    elif x < y:
        soma_impares(x, y)
    else:
        soma_impares(y, x)
