print('=-'*20)
print('              MERCADO')
print('=-'*20)
cont = 0
somaC = 0
mi = 0
mp = 0
nomeB = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    if preco > 1000:
        mi += 1

    cont += 1

    if cont == 1 or preco < mp:
        mp = preco
        nomeB = nome

    somaC = somaC + preco

    res = str(input('Deseja continuar (S / N): ')).upper()
    if res == 'N':
        break
print('O total gasto foi {}'.format(somaC))
print('São {} produto(s) custam R$1000'.format(mi))
print('O produto mais barato é {} que custou R${}'.format(nomeB, mp))

