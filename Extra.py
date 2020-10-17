def tic_tac_toe(board,sign,place):
    sign='non'
    i=0
    place='non'
    board=['','','','','','','','','','']
    game = True
    def display_board(board):
        print(board[0])
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-----')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-----')
        print(board[7] + '|' + board[8] + '|' + board[9])
    display_board(board)

    def win(board, sign):
        return (board[1] == sign and board[2] == sign and board[3] == sign) or \
               (board[4] == sign and board[5] == sign and board[6] == sign) or \
               (board[7] == sign and board[8] == sign and board[9] == sign) or \
               (board[1] == sign and board[4] == sign and board[7] == sign) or \
               (board[2] == sign and board[5] == sign and board[8] == sign) or \
               (board[3] == sign and board[6] == sign and board[9] == sign) or \
               (board[1] == sign and board[5] == sign and board[9] == sign) or \
               (board[3] == sign and board[5] == sign and board[7] == sign)
    win(board,sign)

    while game:
        while i<9:
            while place not in ('1','2','3','4','5','6','7','8','9'):
                print("board positions - ('1','2','3','4','5','6','7','8','9')")
                place=input("Enter your desirable location on board:- ")
                if place not in ['1','2','3','4','5','6','7','8','9'] or board[int(place)] !='':
                    print('Invalid entry.\nTry again.')
                else:
                    while sign not in ('x','X','o','O'):
                        sign=input("enter your sign/mark ('X','O'):- ")
                        if sign not in ('x','X','o','O'):
                            print("Try again.\n")
                        else:
                            print("")
                            board[(int(place))]=sign
                    display_board(board)
                    result = win(board, sign)
                if result == True:
                    print(f'Player {sign} is winner.')
                    i=10
            place=''
            sign=''
            i=i+1
        if i>=9:
            game=False
    if result==False:
        print("The Game is tie.")
tic_tac_toe(board=0,sign=0,place=0)