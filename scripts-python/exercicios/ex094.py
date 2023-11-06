pessoa = dict()
pesquisa = list()
#pesquisa = [{'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 40}, {'Nome': 'Pedro', 'Sexo': 'M', 'Idade': 22}, {'Nome': 'Maria', 'Sexo': 'F', 'Idade': 33}, {'Nome': 'Paula', 'Sexo': 'F', 'Idade': 12}]
soma = media = 0
maiorM = 0


while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')

    pessoa['Idade'] = int(input('Idade: '))
    pesquisa.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Digite S ou N')
    if resposta in 'nN':
        break

print(pesquisa)
for p in pesquisa:
    for k, v in p.items():
        if k in 'Idade':
            soma += v

media = soma / len(pesquisa)


print('=-' * 20)
print(f' - O grupo tem {len(pesquisa)} pessoas')
print(f' - A média de idade é de {media:.2f} anos')
print(' - As mulheres cadastras foram: ', end='')
for p in pesquisa:
    for k, v in p.items():
        if k in 'Sexo' and v in 'fF':
            print(p['Nome'], end=' ')
print()
print(' - Lista das pessoas que estão acima da média:')
for p in pesquisa:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'   {k} = {v};', end=' ')
        print()
print(' ENCERRADO')


