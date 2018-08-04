a = 1

while a==1:
    player1 = input('Player 1 - Rock, Paper or scisors?')
    player2 = input('Player 2 - Rock, Paper or scisors?')

    if 'oc' in player1 or 'OC' in player1:
        if 'oc' in player2 or 'OC' in player1:
            print ('ITS A DRAW')
        elif 'pe' in player2 or 'PE' in player2:
            print('PLAYER 2 IS THE WINNER')
        elif 'so' in player2 or'SO' in player2:
            print('PLAYER 1 IS THE WINNER')

    elif 'pe' in player1 or 'PE' in player1:
        if 'pe' in player2 or 'PE' in player1:
            print ('ITS A DRAW')
        elif 'so' in player2 or 'SO' in player2:
            print('PLAYER 2 IS THE WINNER')
        elif 'oc' in player2 or 'OC' in player2:
            print('PLAYER 1 IS THE WINNER')

    elif 'so' in player1 or 'SO' in player1:
        if 'so' in player2 or 'SO' in player2:
            print ('ITS A DRAW')
        elif 'ro' in player2 or 'RO' in player2:
            print('PLAYER 2 IS THE WINNER')
        elif 'pe' in player2 or 'PE' in player2:
            print('PLAYER 1 IS THE WINNER')

    else:
        print('If you want to play, TYPE IT RIGHT')

    play_again = input('Do you want to play again? Type No if you want to quit')

    if 'n' in play_again or 'N' in play_again or 'o' in play_again:
        a = 0
        print('Thank you for playing!')

    elif 'es' in play_again:
        print('Lets do this!')
        
    else:
        print('If you want to quit type no, otherwise YOU ARE PLAYING AGAIN')
        print('LETS GOOOOO!')
