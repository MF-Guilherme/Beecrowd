def percentual_cobaia(cobaia, total_cobaias):
    resultado = cobaia / total_cobaias * 100
    return resultado


total_cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

n = int(input())
for i in range(n):
    qtd, tipo = map(str, input().split(' '))
    total_cobaias += int(qtd)
    if tipo == 'C':
        coelhos += int(qtd)
    elif tipo == 'R':
        ratos += int(qtd)
    else:
        sapos += int(qtd)

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_cobaia(coelhos,total_cobaias):.2f} %')
print(f'Percentual de ratos: {percentual_cobaia(ratos, total_cobaias):.2f} %')
print(f'Percentual de sapos: {percentual_cobaia(sapos, total_cobaias):.2f} %')
