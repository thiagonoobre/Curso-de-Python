lista = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        #lista[i][c]= int...
        valor = int(input(f'Digite um valor [{i}, {c}]: '))
        lista[i].append(valor)


print('=' * 25)
print(lista[0])
print(lista[1])
print(lista[2])

