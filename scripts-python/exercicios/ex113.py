def leiaInt(msg):
    while True:
        try:
            valor = input(msg)
            if valor == '':
                print('O usuario preferiu não digitar valor')
                return 0
                break
            else:
                va = int(valor)
        except:
            print('\033[1:31mERRO! Digite um numero inteiro válido\033[m')
            continue
        else:
            return va



def leiafloat(msg):
    while True:
        try:
            valor = input(msg)
            if valor == '':
                print('O usuario preferiu não digitar valor')
                return 0
                break
            else:
                va = float(valor)
        except:
            print('\033[1:31mERRO! Digite um numero flutuante válido\033[m')
            continue # retorna para while
        else:
            return va


ni = leiaInt('Digite um numero: ')
print(f'Você acabou de digirar o numero {ni}')

nf = leiafloat('Digite um numero: ')
print(f'Você acabou de digirar o numero {nf}')
