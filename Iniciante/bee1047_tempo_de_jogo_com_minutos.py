def calculo_minutos(inicial, final):
    minuto_total = 0
    if inicial == final:
        return minuto_total
    elif inicial < final:
        total = final - inicial
        return total
    else:
        total = 60 - minuto_inicial + minuto_final
        return total


hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

durou_24h = hora_inicial == minuto_inicial == hora_final == minuto_final

if durou_24h:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')    
elif hora_inicial == hora_final and minuto_inicial < minuto_final:
    hora_total = hora_final - hora_inicial
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
elif hora_inicial == hora_final and minuto_inicial > minuto_final:
    hora_total = 24 - hora_inicial + hora_final - 1
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
elif hora_inicial < hora_final and minuto_inicial > minuto_final:
    hora_total = hora_final - hora_inicial - 1
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
elif hora_inicial < hora_final and minuto_inicial < minuto_final:
    hora_total = hora_final - hora_inicial
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
elif hora_inicial > hora_final and minuto_inicial > minuto_final:
    hora_total = 24 - hora_inicial + hora_final - 1
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
else:
    hora_total = 24 - hora_inicial + hora_final
    minuto_total = calculo_minutos(minuto_inicial, minuto_final)
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')
