lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutaveis ou seja não podem mudar
# e tiver rodando o programa

print(lanche)
print(lanche[-3:])
print(lanche[:2])
print(lanche[2:])


# 3 maneiras para sair o mesmo resultado
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


for comida in lanche:
    if comida in 'Suco':
        print(f'Eu vou bebe {comida}')
    else:
        print(f'Eu vou comer {comida}')


for pos, comida in enumerate(lanche):
    if comida in 'Suco':
        print(f'Eu vou bebe {comida} na posição {pos}')
    else:
        print(f'Eu vou comer {comida} na posição {pos}')


# Coloca em odem alfabetica sua tupla
print(sorted(lanche))




print('Comi pra caramba')
