
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
   try:
       a = open(nome, 'wt+')
       a.close()
   except:
       print('Houve um ERRO na criação do aquivo!')
   else:
       print(f'Aquivo {nome} criado com sucesso')


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o aquivo')
    else:
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0].upper()}', end='')
            tira = len(dados[0])
            print(f'{dados[1]} anos'.rjust(50 - tira))
    finally:
        a.close()


def castrar(arquivo, nome, idade):

    while True:
        n = input(nome)
        if n == '':
            print('\033[1:31mERRO! Por favor verifique se você digitou o NOME correto\033[m')
        elif n.isnumeric():
            print('\033[1:31mERRO! Por favor verifique se você digitou o NOME correto\033[m')
        else:
            break

    while True:
        i = input(idade)
        try:
            valor = int(i)
        except:
            print('\033[1:31mERRO! Por favor insira um numero INTEIRO  válido\033[m')
        else:
            break

    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{n};{valor}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {n} adcionado')
        a.close()






