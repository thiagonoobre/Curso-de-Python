def função(fun):
    nome = 'Acessando o manual do comando'
    print('\033[0:30:46m~' * (len(nome) + len(fun) + 6))
    print(f"  {nome} '{fun}' ")
    print('~' * (len(nome) + len(fun) + 6))
    print(f'\033[7:31:40m')
    print(help(fun))
    print('\033[0m')





while True:
    nome = 'SISTEMA DE AJUDA PyHELP'
    print('\033[0:30:43m~' * (len(nome) + 4))
    meio = len(nome) + 4
    print(f'{nome:^{meio}}')
    print('~' * (len(nome) + 4))
    print('\033[0m')
    f = str(input('Função ou Biblioteca > '))

    if f in 'fimFIM':
        nome = 'ATÉ LOGO'
        print('\033[0:30:42m~' * (len(nome) + 4))
        meio = len(nome) + 4
        print(f'{nome:^{meio}}')
        print('~' * (len(nome) + 4))
        print('\033[0m')
        break

    função(f)
