def leiaDinheiro(msg):
    val = False
    while not val:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um preço invalido')
        else:
            val = True
            return float(entrada)
