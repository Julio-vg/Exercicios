# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
# litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def menu():
    print('''-------------------------------------------------------\n\n\n
1) Deseja Comprar Apenas Latas de 18 Litros
2) Deseja Comprar Apenas Galões de 3,6 Litros
3) Deseja Misturar as Latas e Galões\n\n\n
-------------------------------------------------------\n''')
    while True:
        try:
            escolha = int(input('Escolha Uma Das Opções Acima: '))
            if escolha == 1:
                totalLatas = int(input('Informe a Quantidade de Latas: '))
                totalpreco = totalLatas * 80
                print(f'O Total Da Compra Será R$ {totalpreco}.')
                break
            elif escolha == 2:
                totalGaloes = int(input('Informe a Quantidade de Galões: '))
                totalpreco = totalGaloes * 25
                print(f'O Total da Compra Será R$ {totalpreco}.')
                break
            elif escolha == 3:
                totalLatas = int(input('Informe a Quantidade de Latas: '))
                totalGaloes = int(input('Informe a Quantidade de Galões: '))
                totalprecoL = totalLatas * 80
                totalprecoG = totalGaloes * 25
                total = totalprecoL + totalprecoG
                print(f'O Total da Compra Será R$ {total}.')
                break
            elif escolha >= 4 or escolha <=0:
                print('Opção Invalida!')
        except:
            print('Opção Invalida!')

while True:
    try:
        area = float(input('Informe o tamanho da area a ser pintado: '))
    except:
        print('Valor Invalido!', '\n', 'Digite um Valor Valido')

    else:
        break


def preco():
    folga = area / 6 * 10/100
    tinta = area / 6 + folga
    print(f'Quantidade de Tinta necessario é {round(tinta)} Litros')
    menu()


preco()

