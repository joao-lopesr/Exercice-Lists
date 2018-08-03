numero = 600851475143

lista_primos = []

divisor = 2

while (numero > 1):
    while numero % divisor == 0:
        lista_primos.append(divisor)
        numero /= divisor

    divisor = divisor + 1

for i in lista_primos:
    print (i)
    
print (max(lista_primos))



