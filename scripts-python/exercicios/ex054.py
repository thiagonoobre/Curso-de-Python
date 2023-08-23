from datetime import date
anoat = date.today().year

a = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if anoat - ano <= 18:
        a = a + 1
print('Tem {} que ainda não atigiram a maioridade'.format(a))