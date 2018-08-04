print('Type below the size of the board desired:')

colums = int(input('Type the number of colums:')) 
line = int(input('Type the number of lines:'))

print (colums * ' ---')
for i in range(line+1):
    
    print ('|'+colums * '   |')
    print (colums * ' ---')
    

    
