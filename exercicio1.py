# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$


import math

trabalhador = []


def trabalho():
    while True:
        try:
            horas = float(input('Quantidade do salario por hora: '))
            trabalhador.append(horas)
            horasTrabalhadas = float(input('Quantas horas trabalhadas?'))
            trabalhador.append(horasTrabalhadas)
        except:
            print('Insira um valor valido!')
        else:
            break


def descontos():
    salarioBruto = math.prod(trabalhador)
    INSS = salarioBruto * (8/100)
    IR = salarioBruto * (11/100)
    sindicato = salarioBruto * (5/100)
    salarioLiquido = salarioBruto - INSS - IR - sindicato
    print(f'''Seu Salario Bruto é de R$ {round(salarioBruto)}
Desconto do INSS de R$ {round(INSS)} 
Desconto do Imposto de Renda de R$ {round(IR)} 
Desconto do Sindicato de R$ {round(sindicato)} 
Seu Salario Liquido é de R$ {round(salarioLiquido)}''')


trabalho()
descontos()
