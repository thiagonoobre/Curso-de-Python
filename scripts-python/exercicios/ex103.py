def ficha(nome='<Desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


n = str(input('Nome do jogador: '))
g = str(input('Numero de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
