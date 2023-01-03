n = int(input())

horas = 0
minutos = 0
segundos = 0

while n > 0:
    if n >= 3600:
        horas += 1
        n -= 3600
    elif n >= 60:
        minutos += 1
        n -= 60
    else:
        segundos = n
        n = 0

print(f'{horas}:{minutos}:{segundos}')
