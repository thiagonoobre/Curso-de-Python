''' for c in range(6, 0, -1):
    print(c) '''
'''n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''
''' i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1, p):
    print(c)
print('FIM')'''
s = 0
for c in range(0, 4):
    n = int(input('Digite o valor {}: '.format(c)))
    s += n
print('A soma dos valores é {}'.format(s))
print('FIM')

