def main():
    game_over = False
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player_1_mark, player_2_mark = choose_mark()
    while not game_over:
        board, game_over = player_turn(board, player_1_mark, game_over)
        if not game_over:
            board, game_over = player_turn(board, player_2_mark, game_over)


def display_congrats(board, mark):
    display_board(board)
    print("Congratulations, Player " + mark + ", you have won!")


def check_for_tie(board, game_over):
    if (board[1] != " " and board[2] != " " and board[3] != " " and
       board[4] != " " and board[5] != " " and board[6] != " " and
       board[7] != " " and board[8] != " " and board[9] != " "):
        game_over = True
        display_board(board)
        print("It's a tie!")
    return game_over


def check_for_win(board, mark, game_over):
    if ((board[1] == board[2] == board[3] == mark) or
       (board[4] == board[5] == board[6] == mark) or
       (board[7] == board[8] == board[9] == mark) or
       (board[1] == board[4] == board[7] == mark) or
       (board[2] == board[5] == board[8] == mark) or
       (board[3] == board[6] == board[9] == mark) or
       (board[1] == board[5] == board[9] == mark) or
       (board[3] == board[5] == board[7] == mark)):
        display_congrats(board, mark)
        game_over = True
    else:
        game_over = check_for_tie(board, game_over)
    return game_over


def player_turn(board, mark, game_over):
    display_board(board)
    user_move = " "
    user_move = check_user_move(user_move, board)
    board[user_move] = mark
    game_over = check_for_win(board, mark, game_over)
    return board, game_over


def check_user_move(user_move, board):
    acceptable_range = range(1, 10)
    while (not user_move.isdigit()) or (int(user_move) not in
                                        acceptable_range):
        user_move = input("Please enter a number 1 - 9: ")
    user_move = int(user_move)
    user_move = check_spot(user_move, board)
    return user_move


def check_spot(user_move, board):
    if board[user_move] != " ":
        print("That spot is taken.")
        user_move = input("Please enter a number 1 - 9: ")
    return int(user_move)


def choose_mark():
    player_1_mark = ""
    while player_1_mark != "X" and player_1_mark != "O":
        print("\n" * 100)
        player_1_mark = input("Player 1, please choose X or O: ").upper()
    if player_1_mark == "X":
        return "X", "O"
    else:
        return "O", "X"


def display_board(board):
    print("\n" * 100)
    print(" " + board[1] + " | " + board[2] + " | " + board[3] +
          "             choices:  1 | 2 | 3 ")
    print("-----------                      -----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] +
          "                       4 | 5 | 6 ")
    print("-----------                      -----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] +
          "                       7 | 8 | 9 ")
    print(" ")


if __name__ == "__main__":
    main()