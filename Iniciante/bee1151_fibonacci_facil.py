n = int(input())

lista = [0, 1]

for i in range(n - 2):
    add = lista[-1] + lista[-2]
    lista.append(add)

for j in lista:
    if j == lista[-1]:
        print(j)
    else:
        print(j, end=" ")