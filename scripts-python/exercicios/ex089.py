pessoa = list()
dado = list()
nota = list()

while True:
    dado.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    dado.append(nota[:])
    nota.clear()
    pessoa.append(dado[:])
    dado.clear()
    resposta = str(input('Deseja continuar? [S/N] R: '))

    if resposta in 'nN':
        break


print('=-' * 30)
print('Num    NOME       MÉDIA')
print('-' * 30, end='')
for i, l in enumerate(pessoa):
    print(f'\n{i}      {pessoa[i][0]:11}', end='')
    print(f'{(pessoa[i][1][0] + pessoa[i][1][1]) / 2:<7.1f}', end='')
print()
print('-' * 30)
while True:
    resposta = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if resposta == 999:
        break
    else:
        print(f'Notas de {pessoa[resposta][0]} são {pessoa[resposta][1]}')

print('FINALIZANDO...')
