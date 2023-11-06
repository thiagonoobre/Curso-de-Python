print('=-'*20)
print('           PROGRAMA DE SOMA')
print('=-'*20)
n = s = 0
print('Ponto de parada: 999')
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n

print('=-'*20)
print(f' A soma vale {s}')
print('=-'*20)