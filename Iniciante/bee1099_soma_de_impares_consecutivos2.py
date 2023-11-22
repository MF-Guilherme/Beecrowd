impares = []
testes = int(input())

for i in range(testes):
    x, y = map(int, input().split(' '))
    if x % 2 != 0:
        impares.append(x)
    if y % 2 != 0:
        impares.append(y)
    