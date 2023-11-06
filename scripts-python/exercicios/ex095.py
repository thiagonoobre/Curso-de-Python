gols = list()
jogador = dict()
dados = list()
#dados = [{'Nome': 'Joelson', 'gols': [3, 2], 'total': 5}, {'Nome': 'Pedrão', 'gols': [2, 0, 4], 'total': 6}, {'Nome': 'Wesley', 'gols': [0, 0, 0, 0], 'total': 0}]
total = 0


while True:
    jogador['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
        jogador['gols'] = gols[:]
        total += gols[c]
        jogador['total'] = total
    total = 0
    gols.clear()

    dados.append(jogador.copy())

    pergunta = str(input('Quer continuar? [S/N] '))
    print('=-' * 40)
    if pergunta in 'nN':
        break




print('=-' * 40)
print('Cod Jogador        Gols           Total', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(dados):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))

    if busca == 999:
        break
    if busca >= len(dados):
        print(f"ERRO! Não existe jogador com código {busca}")
    else:
        print(f' ----LEVANTAMENTO DO JOGADOR {dados[busca]["Nome"]}')
        for i, g in enumerate(dados[busca]['gols']):
            print(f'- Na partida {i+1} marcou {g} gols')
print('Volte sempre!!!')


