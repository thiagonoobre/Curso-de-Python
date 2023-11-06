import datetime
INSS = dict()


INSS['Nome'] = str(input('Nome: '))
anoN = int(input('Ano de Nacimento: '))
ano_atual = datetime.datetime.now().year
INSS['Idade'] = ano_atual - anoN
INSS['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if INSS['ctps'] != 0:
    INSS['Contratação'] = int(input('Ano de contratação: '))
    INSS['Salario'] = float(input('Salário: R$ '))
    INSS['aposentadoria'] = (INSS['Contratação'] + 35) - anoN

print('=-' * 45)
if INSS['ctps'] != 0:
    print(f'Nome tem o valor {INSS["Nome"]}')
    print(f'Idade tem valor {INSS["Idade"]}')
    print(f'CTPS tem valor {INSS["ctps"]}')
    print(f'Contratação tem o valor {INSS["Contratação"]}')
    print(f'Salário tem o valor {INSS["Salario"]}')
    print(f'Aposentadoria tem valor {INSS["aposentadoria"]}')
else:
    print(f'Nome tem o valor {INSS["Nome"]}')
    print(f'Idade tem valor {INSS["Idade"]}')
    print('Não tem carteira de trabalho')