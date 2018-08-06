import random
set1 = set()
set2 = set()

for i in range (random.randrange(30)):
    set1.add (random.randrange(100))
    set2.add(random.randrange(100))

print('7) a.:')
print('Set 1: ',set1)
print('Set 2: ',set2)
print(' ')


union = set1.union(set2)
print('7) b.')
print('Union: ', union)
print(' ')


intersection = set1.intersection(set2)

print('7) c.')
print('Intersection: ', intersection)
print(' ')

symmetric_difference = set1.symmetric_difference(set2)

print('7) d.')
print('Symetric difference: ', symmetric_difference)
print(' ')

print('7) e.')
print('Max set 1: ', max(set1))
print('Max set 2: ', max(set2))
print(' ')
