import dados, menu

arq = 'cursoemvideo.txt'

if dados.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    dados.criarAquivo(arq)



while True:
    menu.menu('MENU PRINCIPAL')
    menu.opções(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    while True:
        op = menu.leiaOpc('\033[1:33mSua Opção:\033[m ')
        if op == 1:
            menu.menu('PESSOAS CADASTRADAS')
            dados.lerAquivo(arq)
        elif op == 2:
            dados.castrar(arquivo=arq, nome='Nome: ', idade='Idade: ')
        elif op == 3:
            break
        else:
            print('\033[1:31mErro! Por favor digite uma opção valida\033[m')
    break


print('\033[1:32m')
menu.menu('PROGRMA FINALIZADO')
print('\033[m')
