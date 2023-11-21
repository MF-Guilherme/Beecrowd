inicio = 5
fim = 2

for i in range(1, 10):
    if i % 2 != 0:
        inicio += 2
        fim += 2
        for j in range(inicio, fim, -1):
            print(f'I={i} J={j}')
            