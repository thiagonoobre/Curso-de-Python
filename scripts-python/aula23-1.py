# TRATAMENTO DE ERRO


#link de todas as exeções em python
# https://docs.python.org/3/library/exceptions.html

try:
    #Operação - Se não occorrer ele vai para exeção
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    # Falhou
    print('Infelizmente tivemos um problema')
    print(f'O problema encontrado foi {erro.__class__}')

else:
    #DEU CERTO
    print(f'O resultado é {r}')

finally:
    #Se der certo ou falhar
    print('Volte sempre!!')
