# Adcionando uma lista dentro de outra lista
#primeiro eu crio a lista dados
dados = list()
dados.append('Pedro')
dados.append(25)
# Nesse caso no idice 1 temos 'Pedro' e no indice 2 temos 25
# Agora vamos criar outra lista chamada pessoas
pessoas = list()
# logo em seguida colocaremos os elementos da lista dados na lista pessoas
pessoas.append(dados[:])# [:] você cria um fatiamento completo da lista dados
#ou seja você adciona todos os elemntos da lista dados na lista pessoas
print(dados) #saida ['Pedro', 25]
print(pessoas) #saida [['Pedro', 25]]
# nesse caso podemos notar que no indice 0 da lista PESSOAS temos os dois
# os dois elementos da lista DADOS

# Podemos adcionar outros elementos na lista
# Nesse caso podemos ver que temos 3 lista dentro da lista PESSOAS
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# No comando abaixo estamos buscando dentro da lista Pessoas o elemento do
# indice 0 e novamente buscando o elemento que conten nessa outra lista de
# indice 0
print(pessoas[0][0])#Saida: Pedro
print(pessoas[0][1])#Saida: 25
print(pessoas[1][1])#Saida: 19
print(pessoas[2][0])#Saida: João
print(pessoas[1])#Saida: ['Maria', 19]
