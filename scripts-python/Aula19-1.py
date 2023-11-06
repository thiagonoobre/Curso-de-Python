#Dicionários
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
# Para CRIAR mais um elemento = Sexo
dados['sexo'] = 'M'
print(dados['sexo'])
# para REMOVER elementos
del dados['idade']
print(dados)

filme = {'Titulo': 'Star Wars',
         'Ano': 1977,
         'Diretor': 'George Lucas'
}

print(filme.values())# Adiciona todos os valores do Dicionario
print(filme.keys())# Adiciona o nome dos elementos EX: 'Titulo'
print(filme.items())# Adiciona os elementos e os valores

# Nesse caso o .items funciona como um enumerate. Sendo e k aparece os Nome dos
# elementos como o .keys, e o v aparece os valores como o comando .values
for k,v in filme.items():
    print(f'O {k} é {v}')
    '''
          O Titulo é Star Wars
          O Ano é 1977
          O Diretor é George Lucas
    '''
