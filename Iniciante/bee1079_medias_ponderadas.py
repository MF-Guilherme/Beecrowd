peso_valor_1 = 2
peso_valor_2 = 3
peso_valor_3 = 5

n = int(input())

for i in range(n):
    n1, n2, n3 = map(float, input().split(' '))
    mp = (n1*peso_valor_1 + n2*peso_valor_2 + n3*peso_valor_3) / (peso_valor_1 + peso_valor_2 + peso_valor_3)
    print(f'{mp:.1f}')
