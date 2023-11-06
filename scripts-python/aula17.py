lanche = ['hamburguer', 'suco', 'pizza', 'picole']

# .append('x') -> adiciona um elemento no final da lista
lanche.append('cookie')
# .insert(posição, 'Elemento') -> adiciona um elemento em uma posição. ]
# Lembrando que se ja tiver um elemnto nessa posição ex: posição 0,
# ele não será excluido, e sim passara a estar na posição sucessora,
# mesma coisa acontece com os proximos elementos
lanche.insert(0, 'Hot Dog')

# Comandos de Remoção de Elementos
# del list[indece] -> remove o elemento no indice indicado
del lanche[3]
# list.pop(indice) -> remove elemento no indice indicado
# normalmente ele é usado para remover o ultimo Elemento da lista
lanche.pop(3) #lanche.pop()
# list.remove('Elemento') -> remove o Elemento indicado
lanche.remove('pizza')
# Todos esse comando quando remove o Elemento, e o Elemento sucessor
# toma seu lugar
# Se voce quiser saber se o elemento está na lista pelo comando
# .remove é só fazer um if como abaixo. Logo se ele não encotar o
# item ele não execulta e evita dar erro no programa.
if 'pizza' in lanche:
    lanche.remove('pizza')

# comando list para criar lista
# para você criar uma lista com valore  você pode usar o range(1,10),
# lembrando que os item no range são ELEMENTOS não o Indice
valores = list(range(4, 11))

# list.sort() -> reorganisa os itens em ordem alfabetica ou numerica
valores.sort()

# list.sort(reverse = True) -> ordena de tras para frente
valores.sort(reverse=True)

# len(list) -> Sabe quantos valores tem na lista
len(valores)

