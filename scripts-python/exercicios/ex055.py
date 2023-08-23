pesoMaior = 0
pesoMenor = 10000
for c in range(0, 5):
    p = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if p > pesoMaior:
        pesoMaior = p
    if p < pesoMenor:
        pesoMenor = p 
print(pesoMaior)
print(pesoMenor)
