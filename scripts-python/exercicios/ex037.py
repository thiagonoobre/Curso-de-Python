print('  CONVERSOR DE BASES NUMERICAS')
print('=' * 33)
n = int(input('Digite um numero inteiro: '))
print('=' * 33)
print('VOCÊ GOSTARIA DE CONVERTE ESSE NUMERO PARA?')
print('1 - \033[1:35m Binario \033[m')
print('2 - \033[1:34m Octal \033[m')
print('3 - \033[1:33m hexadecimal \033[m')
op = int(input('Digite uma das opções: '))

if op == 1:
    print('O numero \033[1:32m {} \033[m em binario é \033[1:35m {} \033[m'.format(n,format(n, 'b')))
elif op == 2:
    print('O numero \033[1:32m {} \033[m em Octal é \033[1:34m {} \033[m'.format(n, format(n, 'o')))
else:
    print('O numero \033[1:32m {} \033[m em Hexadecimal é \033[1:33m {} \033[m'.format(n, format(n, 'x')))

