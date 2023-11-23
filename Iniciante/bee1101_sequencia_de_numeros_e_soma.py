def sequencia(x, y):
    lista = []
    if x >= y:
        for i in range(y, x + 1):
            lista.append(i)
    else:
        for i in range(x, y + 1):
            lista.append(i)
    return lista, sum(lista)

while True:
    m, n = map(int, input().split(' '))
    if m <= 0 or n <=0:
        break
    else:
        seq, soma = sequencia(m, n)
        for item in seq:
            print(item, end=' ')
        print(f'Sum={soma}')