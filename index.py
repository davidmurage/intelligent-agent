import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check for a tie
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# Function to make the computer's move
def computer_move(board, computer, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = computer
                if check_win(board, computer):
                    return row, col
                board[row][col] = " "

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_win(board, player):
                    board[row][col] = computer
                    return row, col
                board[row][col] = " "

    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        if player == "X":
            row, col = map(int, input("Enter your move (row and column): ").split())
        else:
            print("Computer's turn:")
            row, col = computer_move(board, computer, player)

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        player, computer = computer, player

if __name__ == "__main__":
    main()
