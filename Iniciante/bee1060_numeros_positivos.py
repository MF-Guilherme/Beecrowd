count = 0
for i in range(6):
    n = input()
    if not '-' in n:
        count += 1
print(f'{count} valores positivos')
