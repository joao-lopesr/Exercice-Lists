soma = 0
i1 = 1
i2 = 2

while i2 <= 4000000:
    i2 = i2 + i1
    i1 = i2 - i1   

    if i2%2 == 0:
        soma = soma + i2

print (soma)
