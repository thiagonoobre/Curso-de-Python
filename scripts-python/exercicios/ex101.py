
def voto(an):
    from datetime import datetime # ECONOMISA MEMORIA
    idade = datetime.now().year - an
    if idade <= 17:
        return 'Com {idade} anos: NÃO VOTA'
    elif idade > 17 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano_nascimento = int(input('Ano de Nascimento: '))
print(voto(ano_nascimento))


