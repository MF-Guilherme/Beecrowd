hora_inicial, hora_final = map(int, input().split())

durou_24h = hora_inicial == hora_final

if durou_24h:
    print(f'O JOGO DUROU 24 HORA(S)')    
elif hora_inicial > hora_final:
    total = 24 - hora_inicial + hora_final
    print(f'O JOGO DUROU {total} HORA(S)')
else:
    total = hora_final - hora_inicial
    print(f'O JOGO DUROU {total} HORA(S)')
