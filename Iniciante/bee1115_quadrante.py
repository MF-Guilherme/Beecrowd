def quadrante(n1, n2):
    if n1 > 0 and n2 >0:
        print('primeiro')
    elif n1 < 0 and y > 0:
        print('segundo')
    elif n1 < 0 and y < 0:
        print('terceiro')
    else:
        print('quarto')


while True:
    x, y = map(int, input().split(' '))
    if x == 0 or y == 0:
        break
    else:
        quadrante(x, y)