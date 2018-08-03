soma = 0

for i in range(100):
    resto3 = i%3
    resto5 = i%5

    if resto3 == 0 or resto5 == 0:
        soma = soma + i


print (soma)

