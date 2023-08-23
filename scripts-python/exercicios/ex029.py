print('Limite de velocidade de 80km. NÃO ULTRAPASSE ')
km = float(input('Qual a velocidade do carro: '))
if km <= 80.0:
    print('Você está na velocidade ideal')
else:
    m = (km - 80) * 7
    print('VOCÊ FOI MULTADO POR ULTRAPASSA O LIMITE DE VELOCIDADE')
    print('Valor da multa R${:.2f}'.format(m))
