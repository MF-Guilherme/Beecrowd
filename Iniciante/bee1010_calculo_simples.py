cod_p1, qtd_p1, valor_p1 = map(float, input().split(" "))
cod_p2, qtd_p2, valor_p2 = map(float, input().split(" "))

total = valor_p1 * qtd_p1 + valor_p2 * qtd_p2

print(f'VALOR A PAGAR: R$ {total:.2f}')

