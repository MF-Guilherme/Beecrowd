# problema de processamento com os cálculos com numeros de ponto flutuante.


notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0
moedas_05 = 0
moedas_025 = 0
moedas_010 = 0
moedas_005 = 0
moedas_001 = 0

n = float(input())

while n > 0.00:
    if n >= 100.00:
        n -= 100.00
        notas_100 += 1
    elif n >= 50.00:
        n -= 50.00
        notas_50 += 1
    elif n >= 20.00:
        n -= 20.00
        notas_20 += 1
    elif n >= 10.00:
        n -= 10.00
        notas_10 += 1
    elif n >= 5.00:
        n -= 5.00
        notas_5 += 1
    elif n >= 2.00:
        n -= 2.00
        notas_2 += 1
    elif n >= 1.00:
        n -= 1.00
        moedas_1 += 1
    elif n >= 0.50:
        n -= 0.50
        moedas_05 += 1
    elif n >= 0.25:
        n -= 0.25
        moedas_025 += 1
    elif n >= 0.10:
        n -= 0.10
        moedas_010 += 1
    elif n >= 0.05:
        n -= 0.05
        moedas_005 += 1
    else:
        n -= 0.01
        moedas_001 += 1 
print(f'NOTAS:\n'
f'{notas_100} nota(s) de R$ 100.00\n'
f'{notas_50} nota(s) de R$ 50.00\n'
f'{notas_20} nota(s) de R$ 20.00\n'
f'{notas_10} nota(s) de R$ 10.00\n'
f'{notas_5} nota(s) de R$ 5.00\n'
f'{notas_2} nota(s) de R$ 2.00\n'
f'MOEDAS:\n'
f'{moedas_1} moeda(s) de R$ 1.00\n'
f'{moedas_05} moeda(s) de R$ 0.50\n'
f'{moedas_025} moeda(s) de R$ 0.25\n'
f'{moedas_010} moeda(s) de R$ 0.10\n'
f'{moedas_005} moeda(s) de R$ 0.05\n'
f'{moedas_001} moeda(s) de R$ 0.01\n')



