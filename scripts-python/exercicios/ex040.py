print('    CALCULO DE MEDIA ')
print('='*24)
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))

m = (n1 + n2) / 2
if m <= 5:
    print('\033[1:34mREPROVADO\033[m')
elif m > 5 and m < 7:
    print('\033[1:34mRECUPERAÇÃO\033[m')
else:
    print('\033[1:34mAPROVADO\033[m')
print('Sua media foi \033[1:32m{}\033[m'.format(m))