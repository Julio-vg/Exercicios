import math


def menu():
    print('''-------------------------------------------------------\n\n\n
1) Comprar apenas latas\n
2) Comprar apenas galões\n
3) Deseja Misturar as Latas e Galões\n\n\n
-------------------------------------------------------\n''')


while True:
    try:
        area = float(input('Digite a área em m2: '))
        menu()
        escolha = int(input('Escolha Uma Das Opções Acima: '))

        if escolha == 1:
            quantidade_tinta = area / 6
            quantidade_latas = math.ceil(quantidade_tinta / 18)
            preco = quantidade_latas * 80
            print(f'O Total da compra será R$ {preco}.')
            break
        elif escolha == 2:
            quantidade_tinta = area / 6
            quantidade_galoes = math.ceil(quantidade_tinta / 3.6)
            preco = quantidade_galoes * 25
            print(f'O Total da compra será R$ {preco}.')
            break
        elif escolha == 3:
            quantidade_tinta = (area/6) * 1.1
            quantidade_latas, resto_tinta = divmod(quantidade_tinta, 18)
            quantidade_galoes = math.ceil(quantidade_tinta / 3.6)
            preco_lata = quantidade_latas * 80
            preco_galao = quantidade_galoes * 25
            preco_total = preco_lata + preco_galao
            print(f'O Total da compra será R$ {preco_total}.')
            break
        elif escolha >= 4 or escolha <= 0:
            print('Opção Invalida!\nDigite Uma Opção Valida!')
    except ValueError:
        print('Valor Invalido!\nDigite Um Valor Válido!')
