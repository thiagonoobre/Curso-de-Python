print("=" * 25)
print('   PROGRAMA FAZ TUDO')
print('=' * 25)

num = 0
n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input('Digite o Segundo numero: '))

while num == 0:
    print('=' * 25)
    print('         MENU')
    print('=' * 25)
    print('[1] - Somar')
    print('[2] - Mutiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do Programa')
    num = int(input('Qual opção: '))
    print('=' * 25)

    if num == 1:
        r = n1 + n2
        print('A soma dos valores {} e {} tem o resultado de {}'.format(n1, n2, r))
        num = num - 1
    if num == 2:
        r = n1 * n2
        print('A mutiplicação de {} e {} tem o resultado de {}'.format(n1, n2, r))
        num = num - 2

    if num == 3:
        if n1 > n2:
            print('O valor {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O valor {} é maior que {}'.format(n2, n1))
        else:
            print('Os dois valores são iguais')
        num = num - 3

    if num == 4:
        print('Você quiz digitar um novo valor')
        n1 = int(input("Digite o Primeiro numero: "))
        n2 = int(input('Digite o Segundo numero: '))
        num = num - 4
    if num == 5:
        print('=' * 25)
        print('Você decidiu sair do programa')

