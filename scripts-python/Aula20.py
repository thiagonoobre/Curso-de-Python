def mostraLinha():
    print('=-' * 20)


mostraLinha()
print(f'{"Sistema de Alunos":^40}')
mostraLinha()
print(f'{"Cadastro de Funcionarios":^40}')
mostraLinha()
print(f'{"Erro do Sistema":^40}')
mostraLinha()


#COLOCANDO UM  PARAMETRE DENTRO DE UMA FUNÇÃO
def mensagem(msg):
    print('=-' * 20)
    print(msg)
    print('=-' * 20)


mensagem("Sistema de Alunos")

mensagem("BABABA")