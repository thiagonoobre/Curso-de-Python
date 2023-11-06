def notas(*n, sit=False):
    """
    --> Função para analizar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos (ilinitada)
    :param sit: valor opcional, indica se deve ou não adcionar a situação
    :return: dicionario com varias informações sobre a situação da turma
    """
    parametros = dict()
    parametros['Total'] = len(n)
    parametros['Maior'] = max(n)
    parametros['Menor'] = min(n)
    parametros['Media'] = sum(n)/len(n)

    if sit == True:
        if parametros['Media'] < 5:
            parametros['Situação'] = 'RUIM'
        elif 5 < parametros['Media'] < 7:
            parametros['Situação'] = 'RAZOAVEL'
        else:
            parametros['Situação'] = 'BOA'
    return parametros


resp = notas(10, 2.5, 9, 10, sit=True)

print(resp)
