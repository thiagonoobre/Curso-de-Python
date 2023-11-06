n = 0
respo = 's'
r = 0
a = 0
i = 0
menor = 100000
maior = 0
while respo != 'n':
    n = int(input('Digite um numero: '))
    respo = str(input('Quer digitar um numero? [s/n] '))
    r = n + a
    a = r
    i += 1
    if n < menor:
        menor = n
    if n > maior:
        maior = n

media = r / i

print('Você digitou {} numeros. \nA media entre os valores é {}'.format(i, media))
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))



