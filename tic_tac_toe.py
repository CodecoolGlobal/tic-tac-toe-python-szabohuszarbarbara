import random
import time

lst = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
'''valid coordinates as a list name(more described)'''


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
    return board

def is_full(board):
    if board[0][0] != '.' and board[0][1] != '.' and board[0][2] != '.' and board[1][0] != '.' and board[1][1] != '.' and board[1][2] != '.' and board[2][0] != '.' and board[2][1] != '.' and board[2][2] != '.':
        return True
    else:
        return False


def get_move(board, player):
    """Returns the coordinates of a valid move for Human on board."""
    move = input("Please make a move!").upper()
    a = 0
    b = 0
    if move == "QUIT":
        quit()
    while move not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
        '''redundant list'''
        print("Invalid move")
        move = input("Please make a move!").upper()
    if move == "A1":
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

def get_random_position(lst):
    '''this function defines the move'''
    move = random.choice(lst)
    return move


def mark(board, player):
    x,y = get_move(board, player)
    if board[x][y] == ".":    
        board[x][y] = player
    else:
        print("This field is taken!")
        print(f"{player}'s turn")
        get_move(board,player)


def new_list(move,lst):
    '''this function takes out the move from the list'''
    while len(lst) > 0:
        lst.pop(lst.index(move))
        return lst


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for AI on board."""
    
    move = get_random_position(lst)
    new_list(move,lst)
    a = 0
    b = 0
    if move == "A1":
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



def marking_AI(board, player):
    while True:
        x, y = get_ai_move(board, player)
        if board[x][y] == '.':
            board[x][y] = player
            break

def has_won1(board, player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col_i in range(len(board)):
        if board[0][col_i] == player and board[1][col_i] == player and board[2][col_i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    return False


def has_won(board, player):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!') 
        return winner   
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        winner = 'X'
        print(f'Player {winner} has won the game!')
        return winner
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        winner = 'O'
        print(f'Player {winner} has won the game!')
        return winner
        
    else:
        return False
    
    


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(f"""
       1   2   3
    A  {board[0][0]} | {board[0][1]} | {board[0][2]}
      ---+---+---
    B  {board[1][0]} | {board[1][1]} | {board[1][2]}
      ---+---+---
    C  {board[2][0]} | {board[2][1]} | {board[2][2]}\n""")


def tictactoe_game():
    board = init_board()
    print_board(board)
    player = 'X'
    while True:
        mark(board, player)
        print_board(board)
        if has_won1(board, player):
            print(f'Player {player} has won the game!')
            break
        if is_full(board):
            print("It's a tie")
            break
        player = 'X' if player == 'O' else 'O'
        print(f"{player}'s turn\n")
        
    

def tictactoe_gameAI():
    board = init_board()
    print_board(board)
    player = 'X'
    while not is_full(board) and not has_won(board, player):
        marking_AI(board, player)
        print_board(board)
        if has_won(board, player):
            break
        if player == 'X':
            player = 'O'
            
        elif player == 'O':
            player = 'X'
        time.sleep(1)

    
    
    if is_full(board) and not has_won(board, player):
        print("It's a tie game")
    

def tictactoe_game_Human_AI():
    board = init_board()
    print_board(board)
    player = 'X'
    while not is_full(board) and not has_won(board, player):
     
        if has_won(board, player):
            break
        if player == 'X':
            mark(board, player)
            print_board(board)
            player = 'O'
            time.sleep(1)
        elif player == 'O':
            marking_AI(board, player)
            print_board(board)
            player = 'X'
            time.sleep(1)

    
    
    if is_full(board) and not has_won(board, player):
        print("It's a tie game")
           

def add_game_mode():
    '''rather choose_game_mode'''
    game_mode = input('''Select a game mode!

    Press 1 for HUMAN - HUMAN
    Press 2 for AI - AI
    Press 3 for HUMAN - AI
    
    For qutting the game type 'Q'
    ''')
    return game_mode
    

def main_menu():
    print(r"""
|\___   ___\\  \|\   ____\        |\___   ___\\   __  \|\   ____\        |\___   ___\\   __  \|\  ___ \     
\|___ \  \_\ \  \ \  \___|        \|___ \  \_\ \  \|\  \ \  \___|        \|___ \  \_\ \  \|\  \ \   __/|    
     \ \  \ \ \  \ \  \                \ \  \ \ \   __  \ \  \                \ \  \ \ \  \\\  \ \  \_|/__  
      \ \  \ \ \  \ \  \____            \ \  \ \ \  \ \  \ \  \____            \ \  \ \ \  \\\  \ \  \_|\ \ 
       \ \__\ \ \__\ \_______\           \ \__\ \ \__\ \__\ \_______\           \ \__\ \ \_______\ \_______\
        \|__|  \|__|\|_______|            \|__|  \|__|\|__|\|_______|            \|__|  \|_______|\|_______|
                                                                                                            
                                                                                                            
                                                                                                            """)




    print('WELCOME TO TIC TAC TOE by THE FRESHMINT TEAM')
    
    mode = add_game_mode()
    valid_input_mode(mode)
 

def valid_input_mode(game_mode):
    if game_mode not in '123Qq':
        print('INVALID INPUT!')
        add_game_mode()
    else:
        if game_mode == '1':
            tictactoe_game()
        elif game_mode == '2':
            tictactoe_gameAI()
        elif game_mode == '3':
            tictactoe_game_Human_AI()
        elif game_mode == 'Q' or 'q':
            quit()

        


if __name__ == '__main__':
    main_menu()


