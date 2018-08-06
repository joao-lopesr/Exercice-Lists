def cap_to_low(letter):

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if letter in a:
        letter = a[a.index(letter)]
        
    elif letter in A:
        letter = a[A.index(letter)]

    return letter


string = input('Type a string:')

new = list(string)

n = int(input('How many of the first letters of the string you desire to convert to small letters:'))

#except ValueError:
#n = int(input('Please, insert an integer:') 

while n > len(string):
    n = int(input('Insert a number smaller or equal to the lenght of the string:'))

for i in range(n):
  new[i] = cap_to_low(new[i])

''.join(new)
print(new)
    
