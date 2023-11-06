'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = [] # valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}... ', end='')
print('\n')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} ')
print('Cheguei o final da lista')
'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))'''

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} ')
print('Cheguei o final da lista')
# Desa maneira as lista ficam interligadas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'lista {a}')
print(f'lista {b}')
# Essa maneira a lista Não fica interligada
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'lista {a}')
print(f'lista {b}')
print(valores.sort())


