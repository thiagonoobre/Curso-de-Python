def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def aumentar(n, p):
    res = n + (n * (p/100))
    return res


def diminuir(n, p):
    res = n - (n * (p/100))
    return res


def metade(n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res