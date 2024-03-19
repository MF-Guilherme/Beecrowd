def area_circulo(raio):
    pi = 3.14159
    return pi * raio**2

raio = float(input())
print(f'A={area_circulo(raio):.4f}')