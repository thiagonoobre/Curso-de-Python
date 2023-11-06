'''brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['UF']) #Rio de Janeiro
print(brasil[1]['Sigla']) #SP
'''
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Metodo para copiar um dicionario,
    # como se fose o [:] das lista

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
        '''
        O campo uf tem valor Rio de Janeiro
        O campo sigla tem valor RJ
        O campo uf tem valor São Paulo
        O campo sigla tem valor SP
        O campo uf tem valor Acre
        O campo sigla tem valor AC
        '''
