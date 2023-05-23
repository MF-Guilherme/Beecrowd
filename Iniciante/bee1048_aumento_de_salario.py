def reajustar(percent):
    reajuste = salario_inicial * percent
    novo_salario = salario_inicial + reajuste
    return novo_salario, reajuste, percent*100

salario_inicial = float(input())

novo_salario = 0.0
reajuste = 0.0
percentual = 0.0

if salario_inicial <= 400.00:
    novo_salario, reajuste, percentual = reajustar(0.15)
elif salario_inicial <= 800.00:
    novo_salario, reajuste, percentual = reajustar(0.12)
elif salario_inicial <= 1200.00:
    novo_salario, reajuste, percentual = reajustar(0.10)
elif salario_inicial <= 2000.00:
    novo_salario, reajuste, percentual = reajustar(0.07)
else:
    novo_salario, reajuste, percentual = reajustar(0.04)
    
print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {int(percentual)} %')
