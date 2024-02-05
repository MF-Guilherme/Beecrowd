x = int(input())
y = int(input())
while y <= x:
    y = int(input())

lista = [x]
i = 1

while sum(lista) < y:
    lista.append(x + i)
    i += 1
    
print(len(lista))