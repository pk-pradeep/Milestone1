a = ['','X','O','X','O','X','O','X','O','X']

# def display_board(board):
#     print(board[0])
#     print(board[1]+'|'+board[2]+'|'+board[3])
#     print('-----')
#     print(board[4]+'|'+board[5]+'|'+board[6])
#     print('-----')
#     print(board[7]+'|'+board[8]+'|'+board[9])

# def x_o():
#     choice='non'
#     while choice not  in ('x','X','o','O'):
#         choice=input('Please enter your choice sign ("X","O"): ')
#         if choice not  in ('x','X','o','O'):
#             print('Sorry! wrong entry...')
#             print('Try again\n')
#     if choice.upper() == 'X':
#         return ('X', 'O')
#     else:
#         return ('O', 'X')


# def user_in(board,sign,position):
#     board[position] = sign

# def win(board,sign):
#     return (board[1] == sign and board[2] == sign and board[3] == sign) or\
#            (board[4] == sign and board[5] == sign and board[6] == sign) or\
#            (board[7] == sign and board[8] == sign and board[9] == sign) or\
#            (board[1] == sign and board[4] == sign and board[7] == sign) or\
#            (board[2] == sign and board[5] == sign and board[8] == sign) or\
#            (board[3] == sign and board[6] == sign and board[9] == sign) or\
#            (board[1] == sign and board[5] == sign and board[9] == sign) or\
#            (board[3] == sign and board[5] == sign and board[7] == sign)

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
print(choose_first())