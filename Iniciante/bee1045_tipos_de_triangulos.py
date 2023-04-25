def nao_eh_triangulo(a, b, c):
    # se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    if a >= (b + c):
        print('NAO FORMA TRIANGULO')


def triangulo_retangulo(a, b, c):
    # se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')


def triangulo_obtusangulo(a, b, c):
    # se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    if a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    

def triangulo_acutangulo(a, b, c):
    # se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')


def triangulo_equilatero(a, b, c):
    # se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    if a == b and a == c:
        print('TRIANGULO EQUILATERO')


def triangulo_isoceles(a, b, c):
    # se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
    if (a == b and a != c) or (a == c and a != b) or (b == a and b != c) or (b == c and b != a):
        print('TRIANGULO ISOSCELES')


a, b, c = map(float, input().split())

lista = [a, b, c]
lista_ordenada_dec = sorted(lista, reverse=True)

a1, b1, c1 = lista_ordenada_dec

nao_eh_triangulo(a1, b1, c1)
triangulo_retangulo(a1, b1, c1)
triangulo_obtusangulo(a1, b1, c1)
triangulo_acutangulo(a1, b1, c1)
triangulo_equilatero(a1, b1, c1)
triangulo_isoceles(a1, b1, c1)
