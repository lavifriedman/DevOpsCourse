def player_win(game_board):
    for cell_line in game_board:
        for cell in game_board:
            cell_colum = game_board.index(cell_line)
            cell_row = cell_line.index(cell)
            cell_eq_none = cell is None
            cell_win_in_row_one =


def player_win(game_board, cell_colum, cell_row):
    for colum_app in range(4):
        number_of_mache = 0
        for row_app in range(4):
            if number_of_mache == 4:
                return True
            if game_board[cell_colum][cell_row] != game_board[cell_colum + colum_app][cell_row + row_app]:
                continue
            number_of_mache =+ 1
    for row_app in range(4):
        number_of_mache = 0
        for colum_app_app in range(4):
            if number_of_mache == 4:
                return True
            if game_board[cell_colum][cell_row] != game_board[cell_colum + colum_app][cell_row + row_app]:
                continue
                number_of_mache =+ 1
    for app in range(4):
        number_of_mache = 0
        for colum_app_app in range(4):
            if number_of_mache == 4:
                return True
            if game_board[cell_colum][cell_row] != game_board[cell_colum + app][cell_row + app]:
                continue
                number_of_mache =+ 1
    return False