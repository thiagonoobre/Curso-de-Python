def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
        print('FIM!')
        print('=-' * 20)
    elif inicio > fim and passo > 0:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
        print('FIM!')
        print('=-' * 20)
    elif inicio > fim and passo < 0:
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
        print('FIM!')
        print('=-' * 20)
    else:
        print('AAAAAA')




contador(1, 10, 1)
contador(10,0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
