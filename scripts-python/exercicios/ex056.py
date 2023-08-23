novaidade = 0
nomevelho = ''
maioridade = 0
qf = 0
media = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}° pessoa: '.format(c))).strip()
    novaidade = novaidade + idade
    if idade > maioridade and sexo == 'masculino':
        maioridade = idade
        nomevelho = nome
    if idade < 20 and sexo == 'feminino':
        qf = qf + 1
media = novaidade / 4

print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho é {} com {} anos'.format(nomevelho, maioridade))
print('Temos {} mulheres com menos de 20 anos'.format(qf))
