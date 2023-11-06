valores = list()
resposta = 's'

while resposta in 'sS':
    valores.append(int(input('Digite um valore: ')))
    resposta = str(input('Quer condinuar? [S/N] '))

print(f'Foram digitados {len(valores)} numeros')
valores.sort(reverse=True)
print(f'a lista em forma decrecente é {valores}')

if 5 in valores:
    print('Valor 5 foi digitado na lista e está na posição {}'.format(valores.index(5, 0)))
else:
    print('Valor 5 não está na lista')
