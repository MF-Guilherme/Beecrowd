notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

n = int(input())
print(f'{n}')

while n > 0:
    if n >= 100:
        n -= 100
        notas_100 += 1
    elif n >= 50:
        n -= 50
        notas_50 += 1
    elif n >= 20:
        n -= 20
        notas_20 += 1
    elif n >= 10:
        n -= 10
        notas_10 += 1
    elif n >= 5:
        n -= 5
        notas_5 += 1
    elif n >= 2:
        n -= 2
        notas_2 += 1
    else:
        n -= 1
        notas_1 +=1

print(f'{notas_100} nota(s) de R$ 100,00\n'
f'{notas_50} nota(s) de R$ 50,00\n'
f'{notas_20} nota(s) de R$ 20,00\n'
f'{notas_10} nota(s) de R$ 10,00\n'
f'{notas_5} nota(s) de R$ 5,00\n'
f'{notas_2} nota(s) de R$ 2,00\n'
f'{notas_1} nota(s) de R$ 1,00')




