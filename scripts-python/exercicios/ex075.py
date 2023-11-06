
tupla = (int(input('Digite o primeiro numero: ')),
         int(input('Digite o segundo numero: ')),
         int(input('Digite o segundo numero: ')),
         int(input('Digite o quarto numero: ')))
print(tupla)
print('Aparece {} o numero 9'.format(tupla.count(9)))

if 3 in tupla:
    print('O numero 3 aparece na {}° posição'.format(tupla.index(3)+1))
else:
    print('O numero 3 não aparece em nenhuma posição')


i = 0
print('Os numeros pares são: ', end=' ')
for i in tupla:
    if i % 2 == 0 and i != 0:
        print('{}  '.format(i), end=' ')


