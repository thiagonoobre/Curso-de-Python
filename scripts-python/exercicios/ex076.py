lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Cardeno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)

print('-' * 40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'\n{lista[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f' R${lista[pos]:>7.2f}')
