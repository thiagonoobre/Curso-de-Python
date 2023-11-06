def soma(a, b):
    s = a + b
    print(s)

soma(b=4, a=5)# MANEIRA DE FINIR NO VALOR DA FUINÇÃO
soma(4, 5)
soma(8, 9)
soma(2, 1)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(b=4, a=5)
soma(7,2)


def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print('Fim!')


contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valor {num} e são ao todo {tam} numeros')


contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)

#DESENPACOTAMENTO
def somaD(*valoresD):
    s = 0
    for num in valoresD:
        s += num
    print(f'Soma dos valores {valoresD} temos {s}')


somaD(5, 2)
somaD(2, 9, 4)



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
