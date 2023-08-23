nome = str(input('Qual é seu nome? '))
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é Legal!')
print('Tenha um bom dia {}{}{}'.format('\033[4:36m',nome,'\033[m'))
