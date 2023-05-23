def impostoDeRenda(salario):
    imposto = 0.0
    if salario <= 2000.0:
        return 'Isento'
    elif salario <= 3000.0:
        imposto = ((salario - 2000.0) * 0.08)
    elif salario <= 4500.0:
        imposto = ((salario - 3000.0) * 0.18) + (0.08 * 1000)
    else:
        imposto = ((salario - 4500.0) * 0.28) + (0.18 * 1500.0) + (0.08 * 1000)
    return f'R$ {imposto:.2f}'
        

salario = float(input())

print(impostoDeRenda(salario))


