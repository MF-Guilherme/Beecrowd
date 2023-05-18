a, b, c = map(float, input().split())

lista = [a, b, c]
lista_ordenada_dec = sorted(lista, reverse=True)

a, b, c = lista_ordenada_dec

if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')
elif (a == b and a != c) or (a == c and a != b) or (b == a and b != c) or (b == c and b != a):
    print('TRIANGULO ISOSCELES')
