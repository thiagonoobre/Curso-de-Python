s = str(input('Digite o sexo: ')).upper()

while s != 'M' and s != 'F':
    print('Você digitou o sexo errado')
    s = str(input('Digite o sexo: ')).upper()
print('Fim!')
