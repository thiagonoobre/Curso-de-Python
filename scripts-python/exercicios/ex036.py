print('=' * 26)
print('   EMPRÉSTIMO BANCÁRIO')
print('=' * 26)
valorcasa = float(input("Qual o valor da Casa? "))
salario = float(input('Qual seu salario: '))
anos = int(input('Quantos anos você vai pagar: '))

valorParcela = valorcasa / (anos * 12)

porc = salario * (30/100)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será R${:.2f}'.format(valorcasa, anos, valorParcela))

if valorParcela <= porc:
    print('=' * 26)
    print('PARABENS!!!')
    print('VOCÊ PODE FINANCIAR A CASA')
    print('=' * 26)
else:
    print('=' * 40)
    print('INFELIZMENTE VOCÊ NÃO VAI PODER FINANCIAR A CASA')
    print('=' * 40)
