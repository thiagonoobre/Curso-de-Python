try:
    #Operação - Se não occorrer ele vai para exeção
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por ZERO')
except KeyboardInterrupt:
    print('O Usuario preferiu não informa os dados!')
except Exception as erro:
    print(f'O erro encotrado foi {erro.__cause__}')
else:
    #DEU CERTO
    print(f'O resultado é {r}')

finally:
    #Se der certo ou falhar
    print('Volte sempre!!')
