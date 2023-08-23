print('==== CALCULADORA DE DESCONTO =====')
v = float(input('Digite o valor do produto: '))
d = float(input('Digite o valor do desconto: '))

n = v - (v * (d / 100))

print('O valor com desconto custa R${:.2f}'. format(n))
