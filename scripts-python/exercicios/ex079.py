valores = list()
resposta = 's'

while resposta in 'sS':
    v = int(input('Digite um valor: '))
    if v in valores:
        print('Valor duplicado! Não vou adcionar ...')
    else:
        print('Valor adcionado com sucesso!')
        valores.append(v)
    resposta = str(input('Quer condinuar? [S/N] '))
valores.sort()
print('Você digitou os valores {}'.format(valores))

# OUTRA MANEIRA

numero = list()
'''
while True:
    n = int(input('Digite um numero: '))
    if n not in numero:
        numero.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break'''