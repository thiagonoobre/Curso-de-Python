a = float(input('Digite o valor da reta A: '))
b = float(input('Digite o valor da reta B: '))
c = float(input('Digite o valor da reta C: '))

if a + b > c and b + c > a and a + c > b:

    if a == b and a == c and b == c:
        print('É um triangulo: EQUILÁTERO\033[m')
    elif a == b or a == c or b == c:
        print('É um triangulo: \033[1:34mISÓSCELES\033[m')
    else:
        print('É um triangulo: \033[1:34mESCALENO\033[m')

else:
    print('Não pode forma um triangulo')

