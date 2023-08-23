import math

co = float(input('Digite o CATETO OPOSTO: '))
ca = float(input('Digite o CATETO ADJACENTE: '))

h = math.sqrt((co ** 2) + (ca ** 2))

print('A HIPOTENUSA é {:.2f}'.format(h))
