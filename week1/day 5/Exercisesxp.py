def display_board(board):
    print("\n")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("\n")


def player_input(player, board):
    valid_input = False
    while not valid_input:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)  # Convert move to board coordinates
            if 0 <= move <= 8 and board[row][col] == " ":
                board[row][col] = player
                valid_input = True
            else:
                print("Invalid move, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")


def check_win(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None  


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    turn_count = 0

    while winner is None and turn_count < 9:
        display_board(board)
        player_input(current_player, board)
        winner = check_win(board)

        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break

        current_player = "O" if current_player == "X" else "X"
        turn_count += 1

    if not winner:
        display_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    play()
