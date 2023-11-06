def escreva(pergunta):
    print('~' * (len(pergunta) + 4))
    meio = len(pergunta) + 4
    print(f'{pergunta:^{meio}}')
    print('~' * (len(pergunta) + 4))


perg = str(input('Digite algo: '))
escreva(perg)
