def soma_nao_divisiveis_treze(n1, n2):
    lista_completa = []
    lista_nao_divisiveis = []
    if n2 < n1:
        for i in range(n2, n1 + 1):
            lista_completa.append(i)
    else:
        for i in range(n1, n2 + 1):
            lista_completa.append(i)
    for numero in lista_completa:
        if numero % 13 != 0:
            lista_nao_divisiveis.append(numero)
    return sum(lista_nao_divisiveis)


x = int(input())
y = int(input())

soma = soma_nao_divisiveis_treze(x, y)
print(soma)

