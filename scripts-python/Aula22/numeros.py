from uteis import numeros
# Não é recomendado pelo Python ^^^^^^
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat} ')
print(f'O dobro de {num} é {numeros.dobro(num)} ')
print(f'O tripo de {num} é {numeros.triplo(num)} ')



