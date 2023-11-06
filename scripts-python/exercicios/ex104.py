def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero INTEIRO válido')
        if ok: #aqui ele ja entede que o valor e verdadeiro
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digirar o numero {n}')
