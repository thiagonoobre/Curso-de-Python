print('        CALCULO DO IMC')
print('=' * 30)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (pow(altura, 2))
print('Seu IMC é de \033[1:32m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('Está \033[1:34mABAIXO\033[m do peso')
elif imc >= 18.5 and imc <= 25:
    print('Está no peso \033[1:34mIDEAL\033[m')
elif imc > 25 and imc < 30:
    print('Está no \033[1:34mSOBREPESO\033[m')
elif imc >= 30 and imc <40:
    print('Está com \033[1:34mOBESIDADE\033[m')
else:
    print('Está com \033[1:34mOBESIDADE MÓRBIDA\033[m')

