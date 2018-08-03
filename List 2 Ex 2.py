list = []

print ('Digite 10 numeros')

for i in range(10):
    
    numero = int(input('Faltam '+ str(10-i) + ' numeros:'))
    list.append(numero)


for i in range(10):
    print (list[9-i])
    
