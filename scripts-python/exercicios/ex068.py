print('-='*20)
print('  PROGRAMA DE IMPAR OU PAR COM O PC')
print('-='*20)
from random import randint
vc = 0
while True:
    selec = str(input('Digite oque você quer (PAR / IMPAR): ')).upper()
    print('-='*20)
    comp = randint(0, 10)
    pess = int(input('Digite um valor: '))
    res = comp + pess
    print('-='*20)
    print('Computador esolheu o valor {}'.format(comp))
    print('você escolheu o valor {}'.format(pess))

    print('-='*20)
    print('A soma é {}'.format(res))

    if res % 2 == 0:
        print('RESULTADO: PAR')
        if selec == 'PAR':
            print('VOCÊ GANHOU!!!')
        else:
            print('Você Perdeu :(')
            break

    else:
        print('RESULTADO: IMPAR')
        if selec == 'IMPAR':
            print('VOCÊ GANHOU!!!')
        else:
            print('Você Perdeu :(')
            break
    print('-=' * 20)
    vc += 1

print('Jogador teve {} vitorias consecutivas'.format(vc))
