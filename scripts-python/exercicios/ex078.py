valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valore {cont}: ')))

print(f'Maior valor sendo {max(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
print(f'Menor valor sendo {min(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
print()
