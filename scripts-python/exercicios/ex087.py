lista = [[], [], []]
a = 0
b = 0
for i in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor [{i}, {c}]: '))
        lista[i].append(valor)
        if valor % 2 == 0:
            a += valor

b = lista[0][2] + lista[1][2] + lista[2][2]


c = lista[1][0]
if c < lista[1][1]:
    c = lista[1][1]
if c < lista[1][2]:
    c = lista[1][2]

print('=' * 25)
print(lista[0])
print(lista[1])
print(lista[2])
print('=' * 25)
print(f'A soma dos valores pares é {a}')
print(f'A soma dos valores da terceira coluna é {b}')
print(f'O maior valor da segunda linha é {c}')
