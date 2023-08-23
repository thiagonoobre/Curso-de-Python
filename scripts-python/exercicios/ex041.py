from datetime import date
print('    CATERGORIA DE NATAÇÃO')
print('=' * 30)
a = int((input('Em que ano você nasceu: ')))
ano = date.today().year
an = ano - a
print('Você tem {} anos'.format(an))
if an <= 9:
    print('CATEGORIA: \033[1:34m{} \033[m'.format('MIRIM'))
elif an > 9 and an <= 14:
    print('CATEGORIA: \033[1:34m{} \033[m'.format('INFANTIL'))
elif an > 14 and an <= 19:
    print('CATEGORIA: \033[1:34m{} \033[m'.format('JUNIOR'))
elif an > 19 and an <= 20:
    print('CATEGORIA: \033[1:34m{} \033[m'.format('SÊNIOR'))
else:
    print('CATEGORIA: \033[1:34m{} \033[m'.format('MASTER'))
