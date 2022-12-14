# Name : Lavi Friedman
# Date : 08.12.2022
def check_for_winning(game_board):
    winning_in_square_line_one = (game_board[0][0] == game_board[0][1]) and (game_board[0][1] == game_board[0][2]) \
                                 and (game_board[0][0] != ".")
    winning_in_square_line_two = (game_board[1][0] == game_board[1][1]) and (game_board[1][1] == game_board[1][2]) \
                                 and (game_board[1][1] != ".")
    winning_in_square_line_three = (game_board[2][0] == game_board[2][1]) and (game_board[2][1] == game_board[2][2]) \
                                 and (game_board[2][1] != ".")
    winning_in_square_row_one = (game_board[1][0] == game_board[0][0]) and (game_board[1][0] == game_board[2][0]) \
                                 and (game_board[1][0] != ".")
    winning_in_square_row_two = (game_board[1][1] == game_board[0][1]) and (game_board[1][1] == game_board[2][1]) \
                                and (game_board[1][1] != ".")
    winning_in_square_row_three = (game_board[1][2] == game_board[0][2]) and (game_board[1][2] == game_board[2][2]) \
                                and (game_board[1][2] != ".")
    winning_in_square_angle_line_one = (game_board[1][1] == game_board[0][0]) and (game_board[1][1] == game_board[2][2])\
                                 and (game_board[1][1] != ".")
    winning_in_square_angle_line_two = (game_board[1][1] == game_board[0][2]) and (game_board[1][1] == game_board[2][0])\
                                 and (game_board[1][1] != ".")
    # list of all the possible conditions for winning
    all_the_possible_conditions_for_winning = [
        winning_in_square_line_one,
        winning_in_square_line_two,
        winning_in_square_line_three,
        winning_in_square_angle_line_one,
        winning_in_square_angle_line_two,
        winning_in_square_row_one,
        winning_in_square_row_two,
        winning_in_square_row_three
    ]
    # the function will check  and return True if one of the possible conditions is happening.
    for win_condition in all_the_possible_conditions_for_winning:
        if win_condition:
            return True
    return False


def receive_player_move():
    the_input_is_legal = False
    # this while loop will continue until the player write a legal location of a square in the game board.
    # example for legal input: '1,1'
    while not the_input_is_legal:
        player_move = input("please enter the location of where you want to put your symbol: ")
        square_location = player_move.split(",")
        try:
            square_location[0] = int(square_location[0]) - 1
            square_location[1] = int(square_location[1]) - 1
        # check the player enter a legal input.
        except ValueError:
            print("please enter the square location agine, your last input was illegal.")
            continue
        # check that the input of the player is not out of the game board range.
        if (square_location[0] > 2) or (square_location[0] < 0):
            print('your input is out the range of the game_board')
            continue
        if (square_location[1] > 2) or (square_location[1] < 0):
            print('your input is out the range of the game_board')
            continue
        the_input_is_legal = True
    return square_location


def print_game_board(game_board):
    for square_line in game_board:
        print(square_line[0], ' ', square_line[1], ' ', square_line[2])


def main():
    game_board = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    player_one_symbol = 'X'
    player_two_symbol = 'O'
    number_of_turns = 0  # count the number of turns along the game.
    # This while loop will continue until one of the players is winning or after complete 9 turns.
    while number_of_turns < 9:
        print_game_board(game_board)
        square_location = receive_player_move()
        # Check that the player is not chose a square that was all ready take.
        if game_board[square_location[0]][square_location[1]] != '.':
            print('square', square_location[0] + 1, ',', square_location[1] + 1, 'was all ready take')
            continue
        # put the symbol fo the current player.
        elif number_of_turns % 2 == 0:
            game_board[square_location[0]][square_location[1]] = player_one_symbol
        else:
            game_board[square_location[0]][square_location[1]] = player_two_symbol
        # Check if one of the players is winning.
        if check_for_winning(game_board) and (number_of_turns % 2 == 0):
            print_game_board(game_board)
            return 'player of symbol X is win'
        elif check_for_winning(game_board) and (number_of_turns % 2 == 1):
            print_game_board(game_board)
            return 'player of symbol O is win'
        number_of_turns += 1
    # return this string when there is a tie between the two players.
    return 'no one is win in this game'


if __name__ == '__main__':
    print(main())





