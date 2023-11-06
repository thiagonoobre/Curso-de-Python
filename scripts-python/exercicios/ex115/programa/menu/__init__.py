def linha(tam=50):
    return '-' * tam


def menu(msg):
    print(linha())
    print(f'{msg}'.center(len(linha())))
    print(linha())


def opções(msg):

    for i, v in enumerate(msg):
        print(f'\033[0:33m{i+1} - \033[m',end='')
        print(f'\033[0:34m{v}\033[m')
    print(linha())


def leiaOpc(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1:31mERRO! Digite um numero INTEIRO válido\033[m')
        if ok:  # aqui ele ja entede que o valor e verdadeiro
            break
    return valor