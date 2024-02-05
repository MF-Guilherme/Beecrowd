s = 1
x = 3
y = 2

while not x > 39:
    s += (x / y)
    x += 2
    y *= 2

print(f'{s:.2f}')