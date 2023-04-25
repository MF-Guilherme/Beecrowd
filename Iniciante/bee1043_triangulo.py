def perimetro_triangulo(n1, n2, n3):
    perimetro = n1 + n2 + n3
    return f'Perimetro = {perimetro:.1f}'


def area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return f'Area = {area:.1f}'


a, b, c = map(float, input().split())

lista = [a, b, c]
lista_ordenada = sorted(lista)

if lista_ordenada[0] + lista_ordenada[1] > lista_ordenada[2]:
    print(perimetro_triangulo(a, b, c))
else:
    print(area_trapezio(a, b, c))