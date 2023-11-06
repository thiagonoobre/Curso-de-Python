dado = list()
pessoas = list()
#pessoas = [['Ana', 75.5], ['Pedro', 89], ['Joana', 89], ['Carolina', 55], ['Bianca', 55]]

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    pro = str(input('Deseja continuar: [S/N]'))

    if pro in 'nN':
        break

print(f'Foram cadrastradas {len(pessoas)} pessoas')
######
maior = pessoas[0][1]
for MaiorP in pessoas:
    if MaiorP[1] > maior:
        maior = MaiorP[1]
print(f'O maior peso foi de {maior} KG. Peso de', end='')

for mp in pessoas:
    if mp[1] == maior:
        print(f' {mp[0]} ... ', end='')

print()
#####
menor = pessoas[0][1]
for MenorP in pessoas:
    if MenorP[1] < menor:
        menor = MenorP[1]
print(f'O menor peso foi de {menor} KG. Peso de', end='')

for mep in pessoas:
    if mep[1] == menor:
        print(f' {mep[0]} ... ', end='')
