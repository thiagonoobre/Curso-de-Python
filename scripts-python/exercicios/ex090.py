aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print('=-' * 20)
print(f'O nome é igual a {aluno["Nome"]}')
print(f'Média pe igual a {aluno["Media"]}')
print(f'Situação é igual a {aluno["Situação"]}')
