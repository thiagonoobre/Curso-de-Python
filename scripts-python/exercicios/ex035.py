a = float(input('Digite o valor da reta A: '))
b = float(input('Digite o valor da reta B: '))
c = float(input('Digite o valor da reta C: '))

if a + b > c and b + c > a and a + c > b:
    print('pode forma um triangulo')
else:
    print('Não pode forma um triangulo')
