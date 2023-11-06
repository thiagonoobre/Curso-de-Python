numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Trêses', 'Quatoze', 'Quinze', 'Dezessis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
sg = ''
while True:
    sg = int(input('Digite um numero entre 0 a 20: '))
    if sg == '' or sg > 20:
        sg = int(input('Tente novamente. Digite um numero entre 0 a 20: '))
    if sg < 0:
        break
    print(f'O numero escolhido foi {numero[sg]}')

    