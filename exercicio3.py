
while True:
    try:
        a = float(input('Informe o Primeiro lado: '))
        b = float(input('Informe o Segundo lado: '))
        c = float(input('Informe o Terceiro lado: '))
        break
    except ValueError:
        print('Valor Invalido!')


def comparador():
    if a <= 0 or b <= 0 or c <= 0:
        print('Não Permitido Lados Nulos ou Negativos!')
    elif a + b < c or a + c < b or b + c < a:
        print('Não é um triangulo!')
    elif a == b and b == c:
        print('Triângulo Equilatero.')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')


if __name__ == '__main__':
    comparador()
