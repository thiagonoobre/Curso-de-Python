print('=-'*20)
print('PROGRAMA DE REGISTRO DE DADOS')
print('=-'*20)
pd = 0
h = 0
m = 0
while True:
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o sexo (M / F): ')).upper()
    print('=-' * 20)
    res = str(input('Quer continuar (S / N): ')).upper()
    print('=-' * 20)

    if idade > 18:
        pd += 1
    if sexo == 'M':
        h +=1
    if sexo == 'F' and idade < 20:
        m += 1
    if res == 'N':
        break

print('=-' * 20)
print('Temos {} pessoas com mais de 18'.format(pd))
print('Temos {} Homens que foram cadastrados'.format(h))
print('Temos {} mulheres com menos de 20'.format(m))
