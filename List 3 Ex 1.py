string = input('Please insert a string:')
lenght = int(len(string))
a=1
b=1

for i in range(lenght//2):
    if not string[i] == string[lenght-i-1]:
        b = 0
        a = a*b

if a ==1:
    print ('The string is a palindromonster.')

elif a==0:
    print('The string is not a palindromonster.')
