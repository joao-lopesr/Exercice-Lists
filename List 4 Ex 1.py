def rep_count(string):
    a = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                a.append(j)
    print (a)
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                a[j]=0
    print (a)
    c=0
    for i in range(len(a)):
        if not a[i] == 0:
            c = c+1
    print('This string has ' + str(c) + ' repeated letters')


b = 'thequickbrownfoxjumpsoverthelazydog'
rep_count(b)


