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

def count_number_of_neighbors(row, height, squares):
    neighbors_number = 0
    if squares[row - 1][height - 1] == 'alive':
        neighbors_number += 1
    if squares[row - 1][height] == 'alive':
        neighbors_number += 1
    if squares[row - 1][height + 1] == 'alive':
        neighbors_number += 1
    if squares[row ][height - 1] == 'alive':
        neighbors_number += 1
    if squares[row][height + 1] == 'alive':
        neighbors_number += 1
    if squares[row + 1][height - 1] == 'alive':
        neighbors_number += 1
    if squares[row + 1][height] == 'alive':
        neighbors_number += 1
    if squares[row + 1][height + 1] == 'alive':
        neighbors_number += 1
    return neighbors_number


def main():
    squares = create_squares(100,100)
    set_alive_cells(20,20,squares)
    set_alive_cells(21,20,squares)
    set_alive_cells(20,21,squares)
    print(count_number_of_neighbors(20,20,squares))
    print_the_squares(squares)


if __name__ == "__main__":
    main()