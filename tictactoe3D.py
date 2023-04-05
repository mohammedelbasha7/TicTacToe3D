import random

print(r"""
            _ _                         _                _                            _          _   _            _____   ___   _____ _        _____             _____                                          _ 
  /\  /\___| | | ___     __ _ _ __   __| | __      _____| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  |___ /  /   \ /__   (_) ___  /__   \__ _  ___  /__   \___   ___    __ _  __ _ _ __ ___   ___  / \
 / /_/ / _ \ | |/ _ \   / _` | '_ \ / _` | \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \   |_ \ / /\ /   / /\/ |/ __|   / /\/ _` |/ __|   / /\/ _ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \/  /
/ __  /  __/ | | (_) | | (_| | | | | (_| |  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/  ___) / /_//   / /  | | (__   / / | (_| | (__   / / | (_) |  __/ | (_| | (_| | | | | | |  __/\_/ 
\/ /_/ \___|_|_|\___/   \__,_|_| |_|\__,_|   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| |____/___,'    \/   |_|\___|  \/   \__,_|\___|  \/   \___/ \___|  \__, |\__,_|_| |_| |_|\___\/   
                                                                                                                                                                                   |___/                          
""")
print("Instructions for 3D Tic Tac Toe:\n"
      "1. The player who is X goes first and places their X in any empty square on the grid.\n"
      "2. The player who is O goes next and places their O in any empty square on the 3 grid.\n"
      "3. Players take turns placing their X or O until one player gets three in a row horizontally, vertically, or diagonally on any of the three planes (top to bottom, left to right, front to back) or diagonally through the cube.\n"
      "4. If all squares are filled and no player has three in a row, the game is a tie.\n")

def print_board(board):
    for i in range(3):
        print("Level {}".format(i+1))
        print("   |   |   ")
        print(" {} | {} | {} ".format(board[i][0][0], board[i][0][1], board[i][0][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(board[i][1][0], board[i][1][1], board[i][1][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(board[i][2][0], board[i][2][1], board[i][2][2]))
        print("   |   |   ")

def check_win(board, player):
    # Check rows
    for i in range(3):
        for j in range(3):
            if board[i][j][0] == player and board[i][j][1] == player and board[i][j][2] == player:
                return True

    # Check columns
    for i in range(3):
        for j in range(3):
            if board[i][0][j] == player and board[i][1][j] == player and board[i][2][j] == player:
                return True

    # Check diagonals
    for i in range(3):
        if board[i][0][0] == player and board[i][1][1] == player and board[i][2][2] == player:
            return True
        if board[i][0][2] == player and board[i][1][1] == player and board[i][2][0] == player:
            return True

    # Check levels
    for i in range(3):
        if board[0][0][i] == player and board[1][1][i] == player and board[2][2][i] == player:
            return True
        if board[0][2][i] == player and board[1][1][i] == player and board[2][0][i] == player:
            return True

    # Check cubes
    if board[0][0][0] == player and board[1][1][1] == player and board[2][2][2] == player:
        return True
    if board[0][0][2] == player and board[1][1][1] == player and board[2][2][0] == player:
        return True
    if board[0][2][0] == player and board[1][1][1] == player and board[2][0][2] == player:
        return True
    if board[0][2][2] == player and board[1][1][1] == player and board[2][0][0] == player:
        return True

    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] == ' ':
                    return False
    return True

def get_move():
    level = int(input("Enter level (1-3): ")) - 1
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    return level, row, col



def play_game():
    # Get player names
    name1 = input("Enter name of player 1: ")
    name2 = input("Enter name of player 2: ")
    players = [(name1, 'X'), (name2, 'O')]
    scores = {name1: 0, name2: 0}

    # Initialize board
    board = [[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)]

    # Choose random player to go first
    current_player = random.choice(players)

    # Assign 'X' to first player
    if current_player[1] == 'O':
        players = [(name2, 'X'), (name1, 'O')]
        current_player = players[0]

    while True:
        # Print board
        print_board(board)

        # Get current player's move
        print("It's {}'s turn. ({})".format(current_player[0], current_player[1]))
        level, row, col = get_move()

        # Check if move is valid
        if board[level][row][col] != ' ':
            print("That cell is already occupied. Please try again.")
            continue

        # Make the move
        board[level][row][col] = current_player[1]

        # Check if game is over
        if check_win(board, current_player[1]):
            print_board(board)
            print("{} wins!".format(current_player[0]))
            print(r""" 
   ____                            _         _       _   _                                                             _ 
  / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___     _   _  ___  _   _  __      _____  _ __ | |
 | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|   | | | |/ _ \| | | | \ \ /\ / / _ \| '_ \| |
 | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_  | |_| | (_) | |_| |  \ V  V / (_) | | | |_|
  \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___( )  \__, |\___/ \__,_|   \_/\_/ \___/|_| |_(_)
                   |___/                                                  |/   |___/                                     
""")
            scores[current_player[0]] += 1
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = players[(players.index(current_player) + 1) % 2]

    # Ask for new game
    play_again = input("Do you want to play again? (Y/N) ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Final scores:")
        print("{}: {}".format(name1, scores[name1]))
        print("{}: {}".format(name2, scores[name2]))


play_game()