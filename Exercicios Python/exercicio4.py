import math
while True:
    try:
        num = int(input('Digite um número: '))
        primos = list(range(1, num))
        if num <= 0:
            print('Digite um número positivo e maior que zero!')
        else:
            break
    except ValueError:
        print('Valor Invalido!\nDigite um Valor Válido!')


def primes():
    for i in range(2, int(math.sqrt(num) + 1)):

        if i in primos:
            for x in range(i ** 2, num, i):
                if x in primos:
                    primos.remove(x)

    print(primos)


if __name__ == '__main__':
    primes()
