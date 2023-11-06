# INTERACTIVE HELP
# pode ser usado tanto no Python Console ou como um comando
# usando ele você pode saber para que serve o comando especificando
'help(print)'
# você pode tambem usar o comando DOC
'print(input.__doc__)'

# DOCSTRINGS
# Basicamente o Docstrings ela é criada pelo progrador que está fazendo o
# programa para orientar para que serve aquela função.
def contador(i, f, p):
    """
    I = inicio da contagem
    F = fim da contagem
    P = Passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)
contador(2, 10, 2)


# ARGUMENTOS OU PARAMETRO OPCIONAIS
# Os Parametros Opcionais sever como um valor substituto caso não seja
# informado nenhum valor nos parametros da funnção como por exemplo na
# fuçao de baixo onde o c=0 nesse caso se não for informado nenhum
# valor para C ele vai assumir valor ZERO. Se não tivesse essa opção o
# programa daria ERRO. Podemos colocar outros valores tambem
# não tem problema é "OPCIONAL"
def somar(a, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)


# ESCOPO DE VARIAVEIS
# Como podemos ver abaixo a variavel N como tem ESCOLO GLOBAL ela
# funciona tanto na função quanto no programa pricipal, MAS a variavel
# X como tem um ESCOPO LOCAL só ira funcionar dentro da FUNÇÃO TESTE
def teste():
    x = 8
    print(f'No função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()
"print(f'No programa principal, x vale {x}')"

def teste1(b):
    global a
    # Essa pode ser uma maneira de tranforma a variavel em global
    # que no caso a passa a vale 8 por conta da atribuição abaixo
    # mas antes ela estava valendo 5
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste1(a)
print(f'A fora vale {a}')

# RETORNO DE CONSULTAS
# O comando RETURN faz com que o valor retorne para chamada da função
# na programação principal (ex: somarr(3, 2, 5)), fazendo com que você
# possa colocar esse valor dentro de uma variavel declarar em um print
# e etc
def somarr(a=0, b=0, c=0 ):
    s = a + b + c
    return s


r1 = somarr(3, 2, 5)
r2 = somarr(2, 2)
r3 = somarr(6)
print(f'Meus calculos deram {r1}, {r2} e {r3}')