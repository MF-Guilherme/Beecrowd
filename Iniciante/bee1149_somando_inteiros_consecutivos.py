lista = input().split(" ")
lista_limpa = []

for i in lista:
    if int(i) <= 0:
        pass
    else:
        lista_limpa.append(i)

a, n = lista_limpa

soma = 0
for i in range(int(n)):
   soma += (int(a) + i)

print(soma)

