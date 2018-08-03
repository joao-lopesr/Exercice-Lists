a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_no_rep = []
f = 1

for i in range(len(a)):
    for n in range(len(b)):
        if a[i] == b[n]:
            for k in range(len(list_no_rep)):
                if a[i] == list_no_rep[k]:
                    f = 0
            if f == 1:
                list_no_rep.append(a[i])
        f=1

print(list_no_rep)
