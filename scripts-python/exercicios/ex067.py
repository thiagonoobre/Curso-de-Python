print('=-'*20)
print('         PROGRAMA DE TABUADA')
print('=-'*20)

while True:
    n = int(input('Digite o numero: '))
    if n < 0:
        break

    print('-' * 20)
    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 20)
