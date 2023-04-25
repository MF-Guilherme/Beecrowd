notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0
moedas_50 = 0
moedas_25 = 0
moedas_10 = 0
moedas_5 = 0
moedas_1_centavo = 0

valor = int(float(input()) * 100)

while valor > 0:
    if valor >= 10000:
        valor -= 10000
        notas_100 += 1
    elif valor >= 5000:
        valor -= 5000
        notas_50 += 1
    elif valor >= 2000:
        valor -= 2000
        notas_20 += 1
    elif valor >= 1000:
        valor -= 1000
        notas_10 += 1
    elif valor >= 500:
        valor -= 500
        notas_5 += 1
    elif valor >= 200:
        valor -= 200
        notas_2 += 1
    elif valor >= 100:
        valor -= 100
        moedas_1 += 1
    elif valor >= 50:
        valor -= 50
        moedas_50 += 1
    elif valor >= 25:
        valor -= 25
        moedas_25 += 1
    elif valor >= 10:
        valor -= 10
        moedas_10 += 1
    elif valor >= 5:
        valor -= 5
        moedas_5 += 1
    else:
        valor -= 1
        moedas_1_centavo += 1
        
print(f'NOTAS:\n'
      f'{notas_100} nota(s) de R$ 100.00\n'
      f'{notas_50} nota(s) de R$ 50.00\n'
      f'{notas_20} nota(s) de R$ 20.00\n'
      f'{notas_10} nota(s) de R$ 10.00\n'
      f'{notas_5} nota(s) de R$ 5.00\n'
      f'{notas_2} nota(s) de R$ 2.00\n'
      f'MOEDAS:\n'
      f'{moedas_1} moeda(s) de R$ 1.00\n'
      f'{moedas_50} moeda(s) de R$ 0.50\n'
      f'{moedas_25} moeda(s) de R$ 0.25\n'
      f'{moedas_10} moeda(s) de R$ 0.10\n'
      f'{moedas_5} moeda(s) de R$ 0.05\n'
      f'{moedas_1_centavo} moeda(s) de R$ 0.01')