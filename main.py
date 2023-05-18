from random import randrange

def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for element in row:
            print(element, end=" ")
        print("|")
    print("---------")

def make_user_move(board):
    while True:
        try:
            move = int(input("Digite o número do quadrado que deseja jogar (1-9): "))
            if move < 1 or move > 9:
                print("Número inválido. Tente novamente.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == "O" or board[row][col] == "X":
                print("Campo já ocupado. Tente novamente.")
                continue
            board[row][col] = "O"
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def make_computer_move(board):
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] != "O" and board[row][col] != "X":
            board[row][col] = "X"
            break

def check_game_status(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    if all(element == "O" or element == "X" for row in board for element in row):
        return "Empate"
    return None

def play_game():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print("Bem-vindo ao jogo da velha!")
    print("Você é 'O' e o computador é 'X'.")
    print_board(board)
    while True:
        make_user_move(board)
        print_board(board)
        game_status = check_game_status(board)
        if game_status:
            break
        print("Vez do computador:")
        make_computer_move(board)
        print_board(board)
        game_status = check_game_status(board)
        if game_status:
            break
    if game_status == "Empate":
        print("O jogo terminou em empate.")
    elif game_status == "O":
        print("Parabéns! Você ganhou!")
    elif game_status == "X":
        print("O computador ganhou!")

play_game()