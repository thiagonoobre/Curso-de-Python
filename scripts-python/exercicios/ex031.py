km = float(input('Qual é a distância da viagem em km: '))
if km <= 200:
    v1 = km * 0.50
    print('Sua viagem deu {}km'.format(km))
    print('O valor da sua passagem saiu R${}'.format(v1))
else:
    v2 = km * 0.45
    print('Sua viagem deu {}km'.format(km))
    print('O valor da sua passagem saiu R${}'.format(v2))