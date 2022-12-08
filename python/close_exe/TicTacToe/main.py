# Name: lavi
# Date: 08.12.2022
def check_for_winning(game_board):
    winning_in_square_line_one = (game_board[0][0] == game_board[0][1]) and (game_board[0][1] == game_board[0][2]) \
                                 and (game_board[0][0] != ".")
    winning_in_square_line_two = (game_board[1][0] == game_board[1][1]) and (game_board[1][1] == game_board[1][2]) \
                                 and (game_board[1][1] != ".")
    winning_in_square_line_three = (game_board[2][0] == game_board[2][1]) and (game_board[2][1] == game_board[2][2]) \
                                 and (game_board[2][1] != ".")
    winning_in_square_angle_line_one = (game_board[1][1] == game_board[0][0]) and (game_board[1][1] == game_board[2][2])\
                                 and (game_board[1][1] != ".")
    winning_in_square_angle_line_two = (game_board[1][1] == game_board[0][2]) and (game_board[1][1] == game_board[2][0])\
                                 and (game_board[1][1] != ".")
    all_the_conditions_for_winning = [
        winning_in_square_line_one,
        winning_in_square_line_two,
        winning_in_square_line_three,
        winning_in_square_angle_line_one,
        winning_in_square_angle_line_two
    ]
    for win_condition in all_the_conditions_for_winning:
        if win_condition:
            return True
    return False


def receive_player_move():
    the_input_is_correct = False
    while not(the_input_is_correct):
        player_move = input("please enter the location of where you want to put your symbol: ")
        square_location = player_move.split(",")
        square_location[0] = int(square_location[0]) - 1
        square_location[1] = int(square_location[1]) - 1
        # check that the input of the users is legal.
        if (square_location[0] > 2) or (square_location[0] < 0):
            print('your input is out the range of the game_board')
            continue
        if (square_location[1] > 2) or (square_location[1] < 0):
            print('your input is out the range of the game_board')
            continue
        the_input_is_correct = True
    return square_location


def print_game_board(game_board):
    for square_line in game_board:
        print(square_line)


def main():
    game_board = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    player_one_symbol = 'X'
    player_two_symbol = 'O'
    number_of_turns = 0  # count the number of turns along the game.
    while number_of_turns < 9:
        print_game_board(game_board)
        square_location = receive_player_move()
        # Check that the player is not chose a square that was all ready take.
        if game_board[square_location[0]][square_location[1]] != '.':
            print('this square is all ready take, please choose anther square.')
            continue
        elif number_of_turns % 2 == 0:
            game_board[square_location[0]][square_location[1]] = player_one_symbol
        else:
            game_board[square_location[0]][square_location[1]] = player_two_symbol
        if check_for_winning(game_board) and (number_of_turns % 2 == 0):
            result_of_the_game = 'player of symbol X is win'
            return result_of_the_game
        elif check_for_winning(game_board) and (number_of_turns % 2 == 0):
            result_of_the_game = 'player of symbol O is win'
            return result_of_the_game
        number_of_turns += 1
    return 'no one is win in this game'


if __name__ == '__main__':
    print(main())





