n = int(input())

anos = 0
meses = 0
dias = 0

while n > 0:
    if n >= 365:
        anos += 1
        n -= 365
    elif n >= 30:
        meses += 1
        n -= 30
    else:
        dias = n
        n = 0
print(f'{anos} ano(s)\n'
f'{meses} mes(es)\n'
f'{dias} dia(s)')