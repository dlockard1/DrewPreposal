player_1 = {'s': 1, 'm': 2, 'l': 3}
player_2 = {'s': 1, 'm': 2, 'l': 3}
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#Unsure how to change colors based on the player
def print_board():
    #Creates the board
    #Sets board positions
    #Had to research board ideas
    print('                ')
    print('   +---+---+---+')
    print('   | ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
    print('   +---+---+---+')
    print('   | ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
    print('   +---+---+---+')
    print('   | ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
    print('   +---+---+---+')

def turn_option1(player, size):
    #This is for the place option during a turn
    square_pick = int(input('Enter the number of the square to put Gobbler (1-9, starting in top left corner): '))
    if square_pick == 1:
        row, col = 0, 0
    elif square_pick == 2:
        row, col = 0, 1
    elif square_pick == 3:
        row, col = 0, 2
    elif square_pick == 4:
        row, col = 1, 0
    elif square_pick == 5:
        row, col = 1, 1
    elif square_pick == 6:
        row, col = 1, 2
    elif square_pick == 7:
        row, col = 2, 0
    elif square_pick == 8:
        row, col = 2, 1
    elif square_pick == 9:
        row, col = 2, 2
    else:
        print('Try again.')
        turn_option1(player, size)

    if board[row][col] == ' ' or player[size] > 0:
        board[row][col] = size
        player[size] = 0
    else:
        print('Try again.')
        turn_option1(player, size)



def turn_option2(player, size):
    # This is for the move option during a turn

    while True:
        try:
            old_square = int(input('Enter the current number of the square of the Gobbler: '))
            new_square = int(input('Enter the new number of the square for the Gobbler: '))

            old_row, old_col = get_row_col(old_square)
            new_row, new_col = get_row_col(new_square)

            if board[old_row][old_col] == size and (board[new_row][new_col] == ' ' or is_smaller(board[new_row][new_col], size)):
                board[old_row][old_col] = ' '
                board[new_row][new_col] = size
                break
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid input. Try again.')

def is_smaller(s, m):
    #This allows the player to move a bigger piece on a smaller piece during their "turn_option2"
    sizes = {'s': 1, 'm': 2, 'l': 3}
    return sizes[s] < sizes[m]

def get_row_col(square_pick):
   
    if square_pick == 1:
        return 0, 0
    elif square_pick == 2:
        return 0, 1
    elif square_pick == 3:
        return 0, 2
    elif square_pick == 7:
        return 2, 0
    elif square_pick == 8:
        return 2, 1
    elif square_pick == 9:
        return 2, 2
    else:
        raise ValueError('Invalid square number, enter a number (1-9)')

def check_winner(player):
    #still says that a player wins if 2 different people have 3 in a row. It should ignore unless the same person has 3 in a row
    symbols = [player['s'], player['m'], player['l']]

    for row in range(3):
        if board[row][0] in player.keys() and board[row][1] in player.keys() and board [row][2] in player.keys():
            return True

    for col in range(3):
        if board[0][col] in player.keys() and board[1][col] in player.keys() and board[2][col] in player.keys():
            return True

    if board[0][0] in player.keys() and board[1][1] in player.keys() and board[2][2] in player.keys():
        return True
    if board[0][2] in player.keys() and board[1][1] in player.keys() and board[2][0] in player.keys():
        return True
    return False



def play():
    #This plays the game
    print('Like Tic-Tac-Toe, you must be the first player to get 3 pieces in a row to win. In turn, you can either: 1. Put a new Gobbler on the board, on an empty space or over a smaller Gobbler 2. Move one of your Gobblers already on the board to an empty space or over a smaller Gobbler.')
    print_board()
    while True:
        print('Player 1:')
        print('Your Gobblers:', player_1)
        choice = input('Enter "p" to place a Gobbler, "m" to move a Gobbler: ')
        size = input('Enter the size of Gobbler (s, m, l): ')
        if choice == 'p':
            turn_option1(player_1, size)
        elif choice == 'm':
            turn_option2(player_1, size)
        print_board()
        if check_winner(player_1):
            print('Player 1 wins!')
            break
        print('Player 2:')
        print('Your Gobblers:', player_2)
        choice = input('Enter "p" to place a Gobbler, "m" to move a Gobbler: ')
        size = input('Enter size of Gobbler (s, m, l): ')
        if choice == 'p':
            turn_option1(player_2, size)
        elif choice == 'm':
            turn_option2(player_2, size)
        print_board()
        if check_winner(player_2):
            print('Player 2 wins!')
            break

play()
