tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('=-' * 20)
print('{:^40}'.format('TABELA DO BRASILEIRÃO 2019'))
print('=-' * 20)
print('Digite Quais opções abaixo')
print('A - Apenas os 5 primeiros colocados')
print('B - Os útimos 4 colocados da tabela')
print('C - Uma llista em ordem alfabética')
print('D - Escolha o time para saber a posição dele')
print('E - ')
print('=-' * 20)


while True:
    op = str(input('Opção: ')).strip().upper()
    if op == 'A':
        for c in range(0, 5):
            print(f' {c+1}- {tabela[c]}\n')
            c += 1
            op = ''

    if op == 'B':
        for c in range(16, 20):
            print(f' {c+1}- {tabela[c]}\n')
            c += 1
            op = ''

    if op == 'C':
        print(f' {sorted(tabela)}\n')

    if op == 'D':
        time = str(input('Qual time você gostaria da saber as posição: '))
        print('O {} está na {}° posição'.format(time, tabela.index(time)+1))

    if op == 'E':
        print('Programa finalizado!!')
        break