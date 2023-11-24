def resposta():
    resposta = int(input('Novo grenal (1-sim 2-nao)\n'))
    return resposta

inter = 0
gremio = 0
empates = 0
qtd = 0

while True:
    i, g = map(int, input().split(' '))
    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empates += 1
    qtd += 1
    res = resposta()
    if res != 1:
        break
    else:
        pass

print(f'{qtd} grenais\n'
      f'Inter:{inter}\n'
      f'Gremio:{gremio}\n'
      f'Empates:{empates}')
if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
