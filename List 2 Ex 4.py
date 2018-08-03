print ('Insert 2 STRINGS to be analysed:')

str1 = input('Insert the 1st String:')

str2 = input('Insert the 2nd String:')

print ('String 1:')

print (str1)
print ('Length of String1:' + str(len(str1)) + '\n')


print ('String 2:')

print (str2)
print ('Length of String2:' + str(len(str2)) + '\n')

if len(str1) == len(str2):
    print('The lenght of the Strings are the same')

else:
    print('The lenght of the Strings are different')

if str1 == str2:
    print('The Strings are the same')

else:
    print('The Strings are different')

