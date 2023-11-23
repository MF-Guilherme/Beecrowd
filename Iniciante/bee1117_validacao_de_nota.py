validos = 0
soma = 0
while validos < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        soma += nota
        validos += 1
media = soma / validos
print(f'media = {media:.2f}')