import math

# Initialize the board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw(board):
    return " " not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'O'. AI is 'X'.")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " " or move not in range(9):
                print("Invalid move. Try again.")
                continue
        except:
            print("Invalid input. Enter a number from 1 to 9.")
            continue

        board[move] = "O"
        print_board()

        if check_winner(board, "O"):
            print("You win! 🎉")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI move:")
        print_board()

        if check_winner(board, "X"):
            print("AI wins! 💻")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()