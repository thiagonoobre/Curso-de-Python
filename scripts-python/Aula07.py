# Adição +
# Subtração -
# Muitiplicação *
# divisão /
# Potencia **
# Divisão //
# Resto da Divisão %
# ordem de precedencia:
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

# s = 5 + 3 * 2
# print(s)
# v = 3 * 5 + 4 ** 2
# print(v)
# print(3 * (5 + 4) ** 2)

# nome = input('Qual é seu nome? ')
# print('Pazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
i = n1 // n2
r = n1 % n2
print('Soma vale {}'.format(s))
print('Mutiplicação vale {}'.format(m))
print('Divisao vale {:.3f}'.format(d))
print('Potenciçaõ vale {}'.format(p))
print('Divisão inteira {}'.format(i))
print('Resto da divisão {}'.format(r))




