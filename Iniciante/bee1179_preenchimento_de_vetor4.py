def listas_impar_par():
    for i in range(15):
        entrada = int(input())
        if entrada % 2 == 0:
            lista_pares.append(entrada)
        else:
            lista_impares.append(entrada)

def imprime_e_deleta_pares(l_pares):
    for i, numero in enumerate(l_pares):
        if i <= 4:
            print(f'par[{i}] = {numero}')
    for j in range(5):
        if len(lista_pares) == 0:
            break
        del(lista_pares[0])

def imprime_e_deleta_impares(l_impares):
    for i, numero in enumerate(l_impares):
        if i <= 4:
            print(f'impar[{i}] = {numero}')
    for j in range(5):
        if len(lista_impares) == 0:
            break
        del(lista_impares[0])


lista_pares = []
lista_impares = []

listas_impar_par()

while len(lista_pares) > 0 or len(lista_impares) > 0:
    if len(lista_pares) > 0:
        imprime_e_deleta_pares(lista_pares)
        while len(lista_impares) > 0:
            imprime_e_deleta_impares(lista_impares)
            if len(lista_impares) == 0:
                break
    else:
        imprime_e_deleta_impares(lista_impares)
        while len(lista_pares) > 0:
            imprime_e_deleta_pares(lista_pares)
            if len(lista_pares) == 0:
                break
        


