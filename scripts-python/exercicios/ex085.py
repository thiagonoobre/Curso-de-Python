lista = [[], []]

for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores PARES são {lista[0]}')
print(f'Os valores IMPARES são {lista[1]}')





