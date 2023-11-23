def ordem(n1, n2):
    if n1 < n2:
        print('Crescente')
    else:
        print('Decrescente')

while True:
    x, y = map(int, input().split())
    if x == y:
        break
    else:
        ordem(x, y)