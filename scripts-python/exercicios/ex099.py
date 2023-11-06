def maior(*valores):
    m = 0
    print('=-' * 20)
    print('Analizando os valores passados ...')
    for c in valores:
        print(c, end=' ')
    print(f'Foram informados {len(valores)}  valores ao todo.')
    for c in valores:
        if c > m:
            m = c
    print(f'O maior valor informador foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
