tuple_var = (1, 2, 3, 4, 5, 'a', 'b', 'c')

tuple_var = list(tuple_var)

addition = input('What do you want to add to the tuple: ')

tuple_var.append(addition)

tuple_var = tuple(tuple_var)

print ('This is the new tuple: ', tuple_var)






"""def add_tupple(tuple_var, addition):

    tuple_list = list(tuple_var)
    tuple_list.append(addition)
    new_tuple = tuple(tuple_list)
    
    return new_tuple

addition = input('What do you want to add to the tuple: ')

new_tuple = add_tupple(tuple_var,addition)

print ('This is the new tuple: ', new_tuple)"""
