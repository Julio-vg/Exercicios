
import math

trabalhador = []


def trabalho():
    while True:
        try:
            horas = float(input('Quantidade do salario por hora: '))
            trabalhador.append(horas)
            horas_trabalhadas = float(input('Quantas horas trabalhadas?'))
            trabalhador.append(horas_trabalhadas)
        except ValueError:
            print('Insira um valor valido!')
        else:
            break


def descontos():
    salario_bruto = math.prod(trabalhador)
    inss = salario_bruto * (8/100)
    ir = salario_bruto * (11/100)
    sindicato = salario_bruto * (5/100)
    salario_liquido = salario_bruto - inss - ir - sindicato
    print(f'Seu Salario Bruto é de R$ {round(salario_bruto)}\n'
          f'Desconto do INSS de R$ {round(inss)}\n'
          f'Desconto do Imposto de Renda de R$ {round(ir)}\n'
          f'Desconto do Sindicato de R$ {round(sindicato)}\n'
          f'Seu Salario Liquido é de R$ {round(salario_liquido)}')


if __name__ == '__main__':
    trabalho()
    descontos()
