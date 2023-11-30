saidas = int(input())
contador = 1

for i in range(saidas):
    for j in range(3):
        print(f'{contador}', end=" ")
        contador += 1
        if j == 2:
            print('PUM')
            contador += 1