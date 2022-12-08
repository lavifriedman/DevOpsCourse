def create_squares(length, height):
    squares = []
    for n in range(height):
        squares.append([])
    for cell_line in squares:
        for new_cell in range(length):
            cell_line.append(None)
    return squares


def print_the_squares(squares):
    for n in squares:
        print(n)


def set_alive_cells(row, height, squares):
    squares[row][height] = "alive"


def set_ded_cells(row, height, squares):
    squares[row][height] = None


def count_number_of_neighbors(row, colum, squares):
    neighbors_number = 0
    if (cells_is_not_out_of_squares_range(row - 1, colum - 1, squares)) and (squares[row - 1][colum - 1] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row - 1, colum, squares)) and (squares[row - 1][colum] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row - 1, colum + 1, squares)) and (squares[row - 1][colum + 1] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row, colum - 1, squares)) and (squares[row][colum - 1] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row, colum + 1, squares)) and (squares[row][colum + 1] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row + 1, colum - 1, squares)) and (squares[row + 1][colum - 1] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row + 1, colum, squares)) and (squares[row + 1][colum] == 'alive'):
        neighbors_number += 1
    if (cells_is_not_out_of_squares_range(row + 1, colum + 1, squares)) and (squares[row + 1][colum + 1] == 'alive'):
        neighbors_number += 1
    return neighbors_number


def cells_is_not_out_of_squares_range(row, colum, squares):
    if (row < 0) or (colum < 0) or (len(squares) < row) or (len(squares[0]) < colum):
        return False
    return True


def let_the_user_set_all_the_alive_cells(squares):
    message_for_the_player = """Welcome to the game of life.
    put the locations of where you want put a alive cell over the squares board.
    for start the the hunter games enter 'start'.
    """
    user_finish = False
    print(message_for_the_player)
    while not user_finish:
        user_input = input(': ')
        if user_input == 'start':
            user_finish = True
            continue
        cell_location = user_input.split(',')
        try:
            cell_location[0] = int(cell_location[0])
            cell_location[1] = int(cell_location[1])
        except ValueError:
            print('we put a illegal input, please put a new legal input.')
            continue
        if not cells_is_not_out_of_squares_range(cell_location[0], cell_location[1], squares):
            print('the location you enter is out of range, please choose ather location.')
            continue
        set_alive_cells(cell_location[0], cell_location[1],squares)
    return squares


def main():
    squares = create_squares(10, 10)
    let_the_user_set_all_the_alive_cells(squares)


if __name__ == "__main__":
    main()