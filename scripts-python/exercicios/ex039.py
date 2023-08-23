from datetime import date
print('      PROGRAMA DE ALISTAMENTO')
print('='*36)
nc = str(input('Qual a sua data de nacimento: '))
# d = int(nc[0:2])
# m = int(nc[3:5])
a = int(nc[6:])
ano = date.today().year


if ano - a < 18:
    print('Você ainda vai se alistar ao Serviço Militar')
    print('Falta ainda {} ano(s)'.format( 18 - (ano - a )))
elif ano - a > 18:
    print('Você já passou do tempo de alistamento')
    print('Você passou {} anos'.format((ano - a) - 18))
else:
    print('Você já está no tempo de se alistar')
