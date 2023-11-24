def soma_combustiveis():
    alcool = 0
    gasolina = 0
    diesel = 0

    while True:
        combustivel = int(input())
        if combustivel < 1 or combustivel > 4:
            pass
        elif combustivel == 1:
            alcool += 1
        elif combustivel == 2:
            gasolina += 1
        elif combustivel == 3:
            diesel += 1
        else:
            break
    return alcool, gasolina, diesel

alcool, gasolina, diesel = soma_combustiveis()

print(f'MUITO OBRIGADO\n'
      f'Alcool: {alcool}\n'
      f'Gasolina: {gasolina}\n'
      f'Diesel: {diesel}')
