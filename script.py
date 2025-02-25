import time
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)


    

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"): 
        return 1
    if check_winner(board, "X"):  
        return -1
    if is_full(board): 
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for (i, j) in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "  
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:  
                break
        return best_score
    else:
        best_score = float("inf")
        for (i, j) in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "  
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:  
                break
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False, -float("inf"), float("inf"))
        board[i][j] = " " 
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    print("\nWelcome to the world of Tic-Tac-Toe!")
    print("lets start..!!\n")
    board = [[" " for _ in range(3)] for _ in range(3)]
    compitator = "X"
    ai = "O"

    while True:
        print_board(board)

        row, col = map(int, input(f"Player {compitator} - Enter row and column (0-2): ").split(","))

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = compitator

        if check_winner(board, compitator):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print("\nAI is thinking", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = ai
        print(f"AI placed 'O' at ({ai_row}, {ai_col})")

        if check_winner(board, ai):
            print_board(board)
            print("AI wins,better luck next time...")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
