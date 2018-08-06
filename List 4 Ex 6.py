tuple_var = (1, 2 ,3, 5, 'abc')
n = 1

while n==1:
    i = input('What is in the tuple? ')

    if i.isdigit():
        int_i = int(i)

    if i in tuple_var or int_i in tuple_var:
        print('ITS IN THE TUPLE')
    else:
        print('Its not in the tuple')
        
    u = input('Wanto to test other? (Type no to quit)')
    if 'no' == u or 'No' == u or 'NO' == u:
        print ('Thanks for runnig the program')
        n = 0
