f = str(input('Digite uma Frase: ')).strip()
print('Aparece {} vezes'.format(f.upper().count('A')))
print('Aparece na {} o Ultimo "A"'.format(f.upper().rfind('A')+1))
print('Aparece na {} o primeiro "A"'.format(f.upper().find('A')+1))
