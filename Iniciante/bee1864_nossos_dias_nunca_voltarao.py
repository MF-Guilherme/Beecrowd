n = int(input())

frase = "LIFE IS NOT A PROBLEM TO BE SOLVED"

contador = 1

while contador <= n+1:
    if contador > n:
        print()
        break
    else:
        print(frase[contador-1], end='')
    contador += 1
