x = float(input())
n = [x]

for i in range(99):
    n.append(x / 2)
    x /= 2

for i, numero in enumerate(n):
    print(f'N[{i}] = {numero:.4f}')