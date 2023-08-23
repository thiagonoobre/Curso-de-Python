s = float(input('Digite o Salario do colaborador: '))
if s > 1250.00:
    n1 = s + (s * (10/100))
    print('Seu novo salario é R${}'.format(n1))
else:
    n2 = s + (s * (15/100))
    print('O seu novo salario é R${}'.format(n2))
