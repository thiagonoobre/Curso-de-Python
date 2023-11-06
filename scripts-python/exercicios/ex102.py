def fatorial(num, show=True):
    """
    --> Calcula a faorial de um numero
    :param num: O numero a ser calculado
    :param show: (Opcional) mostar ou não
    :param return: mostra o resultado da fatorial
    """
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):
            f *= c
            print(f'{c}', end='')
            if c != 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
                return f


n = int(input('Digire um numero: '))
p = str(input('Gostaria de mostra o processo? (S/N) '))[0].upper()
if p in 'sS':
    s = True
else:
    s = False
print(fatorial(n, s))
