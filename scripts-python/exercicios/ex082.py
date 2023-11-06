valores = list()
vp = list()
vi = list()
resposta = 's'

while resposta in 'sS':
    valores.append(int(input('Digite um valore: ')))
    resposta = str(input('Quer condinuar? [S/N] '))

for v in valores:
    if v % 2 == 0:
        vp.append(v)
    else:
        vi.append(v)

print(f'A lista criada foi {valores}')
print(f'A lista de numeros PAR é {vp}')
print(f'A lista de numeros IMPAR é {vi}')
