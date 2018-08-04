def evaluate_result(game):
    a = 1
    b = 1
    c = 1
    k = 0

    #verifying if any line has 3 equal signs
    """
    for j in range(2,3):
        if game[0][0] == game[0][j]:
            c = c+1

    for j in range(2,3):
        if game[1][0] == game[1][j]:
            b = b+1

    for j in range(2,3):
        if game[2][0] == game[2][j]:
            c = c+1

    if a ==3:
        print(str(game[0][0]) + ' Player is the winner')
        k = 1
    
    elif b ==3:
        print(str(game[1][0]) + ' Player is the winner')
        k = 1
    elif c ==3:
        print(str(game[2][0]) + ' Player is the winner')
        k = 1
    """

    if game[0][0] == game [0][1] and game[0][0] == game [0][2]:
        print(str(game[0][0]) + ' Player is the winner')
        k = 1
        
    elif game[1][0] == game [1][1] and game[1][0] == game [1][2]:
        print(str(game[1][0]) + ' Player is the winner')
        k = 1
        
    elif game[2][0] == game [2][1] and game[2][0] == game [0][2]:
        print(str(game[2][0]) + ' Player is the winner')
        k = 1


    #verifying if any colum has 3 equal signs

    if game[0][0] == game[1][0] and game [0][0]== game[2][0]:
        print(str(game[0][0]) + ' Player is the winner')
        k = 1

    elif game[0][1] == game[1][1] and game [0][1]== game[2][1]:
        print(str(game[0][1]) + ' Player is the winner')
        k = 1

    elif game[0][2] == game[1][2] and game [0][2]== game[2][2]:
        print(str(game[0][2]) + ' Player is the winner')
        k = 1

    #verifying if ther someone won with a crossed line

    if game[0][0] == game[1][1] and game [0][0]== game[2][2]:
        print(str(game[0][0]) + ' Player is the winner')
        k = 1

    elif game[0][2] == game[1][1] and game [0][2]== game[2][0]:
        print(str(game[0][2]) + ' Player is the winner')
        k = 1

    elif k == 0:
        print('ITS A DRAW')


game = [['X', 'O', ' '], ['O', 'X', ' '], ['O', 'X', 'X']]
evaluate_result(game)

    
    

    
        
