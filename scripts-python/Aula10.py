'''tempo = int(input('Quantos anos seu carro tem: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('fim')'''

'''nome = str(input('Qual é seu nome: '))
if nome == 'Thiago':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1 + n2)/2
print('Sua media foi {:.1f}'.format(m))
if m >= 6:
    print('VOCE FOI APROVADO!!!')
else:
    print('Você foi reprovado :(')
