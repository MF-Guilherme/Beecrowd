saidas = int(input())

for i in range(1, saidas+1):
    print(f'{i} {i**2} {i**3}')
    for j in range(1):
        print(f'{i} {i**2 + 1} {i**3 + 1}')
