board = [' ' for _ in range(9)]

def print_board():
    row1 =    '| {} | {} | {} |'.format(board[0], board[1], board[2])
    colum1='--------------------'
    row2 =    '| {} | {} | {} |'.format(board[3], board[4], board[5])
    colum2='--------------------'
    row3 =    '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(colum1)
    print(row2)
    print(colum2)
    print(row3)
    print()

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def check_draw():
    return ' ' not in board

current_player = 'X'

while True:
    print_board()
    move = input("Jugador {}, Ponga su movimiento (1-9): ".format(current_player))
    if board[int(move) - 1] == ' ':
        board[int(move) - 1] = current_player
        if check_win():
            print_board()
            print("Jugador {} gana!".format(current_player))
            break
        elif check_draw():
            print_board()
            print("Empate!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Movimiento inválido, volve a intentar.")
