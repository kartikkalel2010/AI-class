import random
from colorama import init, Fore, Style

init()  # Initialize colorama

def display_board(board):
    print()
    def colored(cell):
        if cell == "x":
            return Fore.GREEN + cell + Style.RESET_ALL
        elif cell == "o":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return cell
        
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))

def player_choice():
    symbol = ''
    while symbol not in ['x', 'o']:
        symbol = input(Fore.GREEN + "Do you want to be x or o? " + Style.RESET_ALL).lower()
    return (symbol, 'o' if symbol == 'x' else 'x')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    possible_moves = [i for i in range(9) if board[i].isdigit()]
    if possible_moves:
        move = random.choice(possible_moves)
        board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_conditions)

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.YELLOW + f"Congratulations {player_name}, you won!" + Style.RESET_ALL)
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI has won the game!" + Style.RESET_ALL)
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Player'

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()
