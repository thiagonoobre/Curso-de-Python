s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while s != 'M' and s != 'F':
    print('Você digitou o sexo errado')
    s = str(input('Digite o sexo: ')).strip().upper()[0]
print('Sexo {} registado com sucesso!'.format(s))
print('Fim!')
