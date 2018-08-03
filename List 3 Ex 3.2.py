import random
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in range(len(a)):
    a[i] = random.randint(1,100)
    if a[i]%2 == 0:
        b.append(a[i])

print(a)
print(b)
