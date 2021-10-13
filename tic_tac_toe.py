def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
    return board

def is_full(board):
    if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2] != '.':
        return True
    else:
        return False

def moveValidation():
    # ez így még nem tetszik
    move = input("Please make a move!").upper()
    for i in move:
            while i not in "ABC123":
                return False
            else:
                return True


def get_move(board, player):
    move = input("Please make a move!").upper()
    a = 0
    b = 0
    if move == "A1":
<<<<<<< HEAD
        a = 0
        b = 0
    elif move == "A2":
        a = 0
        b = 1
    elif move == "A3":
        a = 0
        b = 2
    elif move == "B1":
        a = 1
        b = 0
    elif move == "B2":
        a = 1
        b = 1
    elif move == "B3":
        a = 1
        b = 2
    elif move == "C1":
        a = 2
        b = 0
    elif move == "C2":
        a = 2
        b = 1
    elif move == "C3":
        a = 2
        b = 2
    return a,b
=======
        row, col = 0, 0
    elif move == "A2":
        row, col = 0, 1
    elif move == "A3":
        row, col = 0, 2
    elif move == "B1":
        row, col = 1, 0
    elif move == "B2":
        row, col = 1, 1
    elif move == "B3":
        row, col = 1, 2
    elif move == "C1":
        row, col = 2, 0
    elif move == "C2":
        row, col = 2, 1
    elif move == "C3":
        row, col = 2, 2
    return row, col
>>>>>>> a806abc6126938cb130ade3d82afd6f51a7769df


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


<<<<<<< HEAD
def mark(board, player):
    x,y = get_move(board, player)    
    board[x][y] = player


def has_won(board, player):
    if board[0][0] and board[0][1] and board[0][2] == 'X':
        winner = 'X'
    elif board[0][0] and board[0][1] and board[0][2] == 'O':
        winner = 'O'    
    elif board[1][0] and board[1][1] and board[1][2] == 'X':
        winner = 'X'
    elif board[1][0] and board[1][1] and board[1][2] == 'O':
        winner = 'O'
    elif board[2][0] and board[2][1] and board[2][2] == 'X':
        winner = 'X'
    elif board[2][0] and board[2][1] and board[2][2] == 'O':
        winner = 'O'
    elif board[0][0] and board[1][0] and board[2][0] == 'X':
        winner = 'X'
    elif board[0][0] and board[1][0] and board[2][0] == 'O':
        winner = 'O'
    elif board[0][1] and board[1][1] and board[2][1] == 'X':
        winner = 'X'
    elif board[0][1] and board[1][1] and board[2][1] == 'O':
        winner = 'O'
    elif board[0][2] and board[1][2] and board[2][2] == 'X':
        winner = 'X'
    elif board[0][2] and board[1][2] and board[2][2] == 'O':
        winner = 'O'
    elif board[0][0] and board[1][1] and board[2][2] == 'X':
        winner = 'X'
    elif board[0][0] and board[1][1] and board[2][2] == 'O':
        winner = 'O'
    elif board[0][2] and board[1][1] and board[2][0] == 'X':
        winner = 'X'
    elif board[0][2] and board[1][1] and board[2][0] == 'O':
        winner = 'O'
    else:
        return False
    
    print(f'Player {winner} has won the game!')
=======
def mark(board, player, row, col):
    board[row][col] = player
    print_board(board)


def has_won(board, player):
    if board[0][0] and board[0][1] and board[0][2] == player:
        winner = player
    elif board[1][0] and board[1][1] and board[1][2] == player:
        winner = player
    elif board[2][0] and board[2][1] and board[2][2] == player:
        winner = player
    elif board[0][0] and board[1][0] and board[2][0] == player:
        winner = player
    elif board[0][1] and board[1][1] and board[1][2] == player:
        winner = player
    elif board[0][2] and board[1][1] and board[2][2] == player:
        winner = player
    elif board[0][0] and board[1][1] and board[2][2] == player:
        winner = player
    elif board[0][2] and board[1][1] and board[2][0] == player:
        winner = player
        
    else:
        return False
    
    

def is_full(board):
    if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2] != '.':
        print('Tie game, GAME OVER!')
        return True
    else:
        return False
>>>>>>> a806abc6126938cb130ade3d82afd6f51a7769df


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(f"""
       1   2   3
    A  {board[0][0]} | {board[0][1]} | {board[0][2]}
      ---+---+---
    B  {board[1][0]} | {board[1][1]} | {board[1][2]}
      ---+---+---
    C  {board[2][0]} | {board[2][1]} | {board[2][2]}\n""")


def print_result(winner):
<<<<<<< HEAD
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass 


def tictactoe_game(mode='HUMAN-HUMAN'):
=======
    print(f'Player {winner} has won the game')


def change_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def tictactoe_game(mode):
>>>>>>> a806abc6126938cb130ade3d82afd6f51a7769df
    board = init_board()
    print_board(board)
    player = 'X'
<<<<<<< HEAD
    while not is_full(board) or not has_won(board, player):
        get_move(board, player)
        mark(board, player)
        print_board(board)
        if player == 'X':
            player = 'O'
        elif player == 'O':
            player = 'X'
        if has_won(board, "X"):
            print("X won the game!")
        elif has_won(board, "O"):
            print("O won the game!")
            break
    if is_full(board):
        print("It's a tie game")
    


        
=======
    printed_board = print_board(board)
    while is_full(board) is False and has_won(board, player) is False:
        row, col = get_move(board, player)
        mark(board, player, row, col)
        player = change_player(player)
    else:
        print_result(winner)
>>>>>>> a806abc6126938cb130ade3d82afd6f51a7769df
    # winner = 0
    # print_result(winner)

def add_game_mode():
    game_mode = input('''Select a game mode!

    Press 1 for HUMAN - HUMAN
    Press 2 for HUMAN - AI
    Press 3 for HUMAN - AI PRO
    Press 4 for AI -AI
    
    For qutting the game type 'Q'
    ''')
    return game_mode
    

def main_menu():
    print('WELCOME TO TIC TAC TOE by THE FRESHMINT TEAM')
     # grafika
    mode = add_game_mode()
    valid_input_mode(mode)
 

def valid_input_mode(game_mode):
    if game_mode not in '1234Qq':
        print('INVALID INPUT!')
        add_game_mode()
    else:
        if game_mode == '1':
            tictactoe_game('HUMAN-HUMAN')
        elif game_mode == '2':
            tictactoe_game('HUMAN-AI')
        elif game_mode == '3':
            tictactoe_game('HUMAN-AI PRO')
        elif game_mode == '4':
            tictactoe_game('AI-AI')
        elif game_mode == 'Q' or 'q':
            quit()

def main():
    main_menu()
    print_board(init_board())
    while True:
        get_move()
        


if __name__ == '__main__':
    main_menu()


