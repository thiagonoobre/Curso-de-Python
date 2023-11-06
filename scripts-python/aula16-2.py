a = (2, 5, 4)
b = (5,8, 1, 2)
c = a + b # essa forma não soma mas junta as duas tuplas
print(c)
# Comando LEN mostra o tamanho da tupla ou STR
print(len(c))
# Count é um metodo para mostrar quantos X elemento está aparecendo
# na tupla
print(c.count(5))
# Index mostra a posição do elemento
print(c.index(8))
# se eu coloco , um numero ele vai tentar achar
# o elemento depois do numero de index colocado
print(c.index(5, 2))

pessoa = ('Gustavo', 38, 'M', 99.88)
print(pessoa)
del(pessoa) #Apaga a tupla
print(pessoa)