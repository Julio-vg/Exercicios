import random
resultados = []

def dados():
    for i in range(100):
        dado = random.randint(1,6)
        resultados.append(dado)
    print(f'O Valor 1 foi gerado: {resultados.count(1)}\n'
          f'O Valor 2 foi gerado: {resultados.count(2)}\n'
          f'O Valor 3 foi gerado: {resultados.count(3)}\n'
          f'O Valor 4 foi gerado: {resultados.count(4)}\n'
          f'O Valor 5 foi gerado: {resultados.count(5)}\n'
          f'O Valor 6 foi gerado: {resultados.count(6)}\n',resultados)


if __name__ == '__main__':
    dados()