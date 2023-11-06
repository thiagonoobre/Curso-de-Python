def area(largura, comprimento):
    a = comprimento * largura
    print(f'a área de um terrenno {largura}X{comprimento} é de {a}m^2')


print('Controle de Terremos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
