str_dia_inicio, dia_inicio = map(str, input().split(' '))
horas_inicio, minutos_inicio, segundos_inicio = map(int, input().split(' : '))
str_dia_fim, dia_fim = map(str, input().split(' '))
horas_fim, minutos_fim, segundos_fim = map(int, input().split(' : '))

w = int(dia_fim) - int(dia_inicio)
x = horas_fim - horas_inicio
y = minutos_fim - minutos_inicio
z = segundos_fim - segundos_inicio

if z < 0:
    z += 60
    y -= 1

if y < 0:
    y += 60
    x -= 1

if x < 0:
    x  += 24
    w -= 1

    
print(f'{w} dia(s)')
print(f'{x} hora(s)')
print(f'{y} minuto(s)')
print(f'{z} segundo(s)')