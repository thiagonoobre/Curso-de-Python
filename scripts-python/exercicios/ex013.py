print('=== REAJUSTE SALARIAL ===')
s = float(input('Digite o salario do colaborador: R$'))
a = float(input('Digite o valor em % do almento: '))

r = s + (s * (a /100))

print('O novo salario do colaborador é de R${:.2f}'.format(r))
