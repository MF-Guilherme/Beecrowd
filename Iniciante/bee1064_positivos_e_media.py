contador_positivos = 0
soma_positivos = 0.0

for i in range(6):
    valor = float(input())

    if valor >= 0:
        contador_positivos += 1 
        soma_positivos += valor

media_positivos = soma_positivos / contador_positivos

print(f'{contador_positivos} valores positivos')
print(f'{media_positivos:.1f}')
