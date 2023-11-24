def lista_divisiveis(n1, n2):
    lista_completa = []
    lista_dos_divisiveis = []
    if n2 < n1:
        for i in range(n2 + 1, n1):
            lista_completa.append(i)
    else:
        for i in range(n1 + 1, n2):
            lista_completa.append(i)
    for numero in lista_completa:
        if numero % 5 == 2 or numero % 5 == 3:
            lista_dos_divisiveis.append(numero)
    return lista_dos_divisiveis


x = int(input())
y = int(input())

lista = lista_divisiveis(x, y)
for i in lista:
    print(i)


