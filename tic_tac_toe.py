import random
import time

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
    move = input("Please make a move!").upper()
    a = 0
    b = 0
    if move == "QUIT":
        quit()
    while move not in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
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

# def get_random_position(lst):
#     move = random.choice(lst)
#     return move

def get_ai_move(board, player):
    all_moves = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    move_index = []
    x, y = get_move(board, player)
    if (x,y) in all_moves:
        all_moves.remove((x,y))
    for i in range(len(all_moves)+1):
        move_index.append(i)
    next_move_index = random.choice(move_index)
    next_ai_move = all_moves[next_move_index]
    return next_ai_move


def mark(board, player):
    x,y = get_move(board, player)
    if board[x][y] == ".":    
        board[x][y] = player
    else:
        print("This field is taken!")
        print(f"{player}'s turn")
        get_move(board,player)
# def new_list(move,lst):
#     while len(lst) > 0:
#         lst.pop(lst.index(move))
#     return lst


# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     lst = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
#     move = get_random_position(lst)
#     new_list(move,lst)
#     a = 0
#     b = 0
#     if move == "A1":
#         a = 0
#         b = 0
#     elif move == "A2":
#         a = 0
#         b = 1
#     elif move == "A3":
#         a = 0
#         b = 2
#     elif move == "B1":
#         a = 1
#         b = 0
#     elif move == "B2":
#         a = 1
#         b = 1
#     elif move == "B3":
#         a = 1
#         b = 2
#     elif move == "C1":
#         a = 2
#         b = 0
#     elif move == "C2":
#         a = 2
#         b = 1
#     elif move == "C3":
#         a = 2
#         b = 2
#     return a,b


def mark(board, player):
    x, y = get_move(board, player)
    if board[x][y] == ".":
        board[x][y] = player

# def marking_AI(board, player):
#     x, y = get_ai_move(board, player)
#     if board[x][y] == ".":
#         board[x][y] = player
      
    
    
def has_won(board, player):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        winner = 'X'
        return winner
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        winner = 'O' 
        return winner   
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        winner = 'X'
        return winner
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        winner = 'O'
        return winner
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
        return winner
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
        return winner
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        winner = 'X'
        return winner
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        winner = 'O'
        return winner
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        winner = 'X'
        return winner
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        winner = 'O'
        return winner
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        winner = 'X'
        return winner
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        winner = 'O'
        return winner
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
        return winner
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
        return winner
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        winner = 'X'
        return winner
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        winner = 'O'
        return winner

    else:
        return False
    
    print(f'Player {winner} has won the game!')
    return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print(f"""
       1   2   3
    A  {board[0][0]} | {board[0][1]} | {board[0][2]}
      ---+---+---
    B  {board[1][0]} | {board[1][1]} | {board[1][2]}
      ---+---+---
    C  {board[2][0]} | {board[2][1]} | {board[2][2]}\n""")


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    print_board(board)
    player = 'X'
    while not is_full(board) and not has_won(board, player):
        mark(board, player)
        print_board(board)
        if has_won(board, player):
            print(f'{player} won the game!')
            break
        if player == 'X':
            player = 'O'
            print("O's turn\n")
        elif player == 'O':
            player = 'X'
            print("X's turn\n")

    if is_full(board) and not has_won(board, player):
        print("It's a tie")
    #if has_won(board, player) and not is_full(board):

# def tictactoe_game(mode=2):
#     board = init_board()
#     print_board(board)
#     player = 'X'
#     while not is_full(board) and not has_won(board, player):
#         marking_AI(board, player)
#         print_board(board)
#         if has_won(board, player):
#             print(f'{player} won the game!')
#             break
#         if player == 'X':
#             player = 'O'
#             time.sleep(1)
#         elif player == 'O':
#             player = 'X'
#             time.sleep(1)

    
    
    if is_full(board) and not has_won(board, player):
        print("It's a tie game")
    

        
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
            tictactoe_game(mode=1)
        elif game_mode == '2':
            tictactoe_game(mode=2)
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
        modvalaszto = add_game_mode()
        if modvalaszto == 1:
            get_move()
        else:
            get_ai_move()
        


if __name__ == '__main__':
    main_menu()


