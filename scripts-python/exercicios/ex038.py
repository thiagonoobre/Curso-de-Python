print('     COMPARADOR  ')
print('='*20)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O \033[1:33mPrimeiro  valor\033[m é \033[1:34mMAIOR \033[m')
elif n2 > n1:
    print('O \033[1:33mSegundo valor\033[m é \033[1:34mMAIOR \033[m')
else:
    print('\033[1:33mNão exsite\033[m valor maior, os dois são \033[1:34mIGUAIS \033[m')
