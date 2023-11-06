def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def aumentar(n, t, sit=True):
    res = n + (n * (t/100))
    return res if sit is False else moeda(res)


def diminuir(n, t, sit=True):
    res = n - (n * (t/100))
    return res if sit is False else moeda(res)



def metade(n, sit=True):
    res = n / 2
    return res if sit is False else moeda(res)


def dobro(n, sit=True):
    res = n * 2
    return res if sit is False else moeda(res)


def resumo(p=0, ta=10, tr=5):
    titulo = 'RESUMO DO VALOR'
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{ta}% de aumento: \t{aumentar(p, ta, True)}')
    print(f'{tr}% de redução: \t{diminuir(p, tr, True)}')
    print('-' * 30)
