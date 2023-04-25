dic = {
    1 : 4,
    2 : 4.5,
    3 : 5,
    4 : 2,
    5 : 1.5
}

cod, qtd = map(int, input().split())

for i in dic:
    if cod == i:
        resultado = dic[i] * qtd

print(f'Total: R$ {resultado:.2f}')
