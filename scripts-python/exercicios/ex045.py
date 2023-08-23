import random

num = random.randint(1, 3)
'''
1 - PEDRA
2 - PAPEL
3 - TESOURA
'''
if num == 1:
    vc = str('PEDRA')
elif num == 2:
    vc = str('PAPEL')
else:
    vc = str('TESOURA')

print('     JOGO DO JOKENPÔ')
print('=' * 25)
print('DIGITE UMA DAS OPÇÕES ')
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
vh = int(input(''))

if vh == 1:
    oph = str('PEDRA')
elif vh == 2:
    oph = str('PAPEL')
else:
    oph = str('TESOURA')

print('O computador escolheu \033[1:34m{}\033[m'.format(vc))
print('Você escolheu \033[1:34m{}\033[m'.format(oph))

if num == vh:
    print('Você EMPATARAM')
elif num != vh and num == 1 and vh == 3:
    print('\033[1:31mVocê PERDEU!!!\033[m')
elif num != vh and num == 2 and vh == 1:
    print('\033[1:31mVocê PERDEU!!!\033[m')
elif num != vh and num == 3 and vh == 2:
    print('\033[1:31mVocê PERDEU!!!\033[m')
else:
    print('\033[1:33mVOCÊ GANHOU!!!\033[m')
    print('\033[1:33mPARABENS\033[m')
