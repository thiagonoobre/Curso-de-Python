print('    CALCULO DE PREÇO DE PRODUTOS')
print('=' * 37)
vl = float(input('Digite o Valor do produto: \033[1:32mR$\033[m '))
print('=' * 37)
print('QUAL A CONDIÇÃO DE PAGAMENTO')
print('1 - À VISTA NO \033[1:34mDINHEIRO / CHEQUE\033[m: \033[1:33m10%\033[m DE DESCONTO')
print('2 - À VISTA NO \033[1:34mCARTÃO\033[m:\033[1:33m5%\033[m DE DESCONTO')
print('3 - \033[1:34mATÉ 2X NO CARTÃO\033[m: PREÇO NORMAL')
print('4 - \033[1:34mATÉ 3X NO CARTÃO\033[m: \033[1:33m20%\033[m DE JUROS')
cd = int(input(''))

if cd == 1:
    vn = vl - (vl * (10/100))
elif cd == 2:
    vn = vl - (vl * (5/100))
elif cd == 3:
    vn = vl
elif cd == 4:
    vn = vl + (vl * (20/100))
else:
    print('Opeção invalida, tente novamente')

if cd <= 4:
    print('Valor do produto vai ficar em \033[1:32mR${}\033[m'.format(vn))
else:
    print('')



