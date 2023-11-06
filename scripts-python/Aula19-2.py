pessoas = {'Nome': 'Thiago', 'Sexo': 'M', 'Idade': 24}
print(pessoas['Nome'])
print(pessoas['Idade'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
# Modifica o valor do Elemento
pessoas['Nome'] = 'João'
# Para adicionar um Elemento
pessoas['Peso']= 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
