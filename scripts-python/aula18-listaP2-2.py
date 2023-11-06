'''teste = list()
teste.append('Thiago')
teste.append(23)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''galera = [['João', 19], ['Ana', 39], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])# printa os NOME das lista

for i in galera:
    print(i[1])# printa as IDADES das lista

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])# Não pode esquecer o [:]
    # se não ele fica ligados
    dado.clear()

# PARA mostar quem é maior de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} Menores de idade')
