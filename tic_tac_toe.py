def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
    
    return board
init_board()

def quit():
    pass

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(board[0][0] + board[0][1] + board[0][2])
    print(board[1][0] + board[1][1] + board[1][2])
    print(board[2][0] + board[2][1] + board[2][2])


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)

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
        if game_mode == 1:
            tictactoe_game('HUMAN-HUMAN')
        elif game_mode == 2:
            tictactoe_game('HUMAN-AI')
        elif game_mode == 3:
            tictactoe_game('HUMAN-AI PRO')
        elif game_mode == 4:
            tictactoe_game('AI-AI')
        elif game_mode == 'Q' or 'q':
            quit()


if __name__ == '__main__':
    main_menu()
