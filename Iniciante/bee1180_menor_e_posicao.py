n = int(input())
x = list(map(int, input().split()))

menor_valor = min(x)
indice = x.index(menor_valor)

print(f'Menor valor: {menor_valor}')
print(f'Posicao: {indice}') 