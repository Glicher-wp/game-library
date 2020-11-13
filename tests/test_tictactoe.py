from games import tictactoe


board_true = [[1, 2, 0],
              [1, 0, 2],
              [2, 1, 2]]

board_false = [[1, 2],
              [1, 0, 2],
              [2, 1, 2]]

board_false_2 = [[1, 2, 0],
                 [1, 0, 2]]

booard_incorrect = [[1, 2, 0],
                    [1, 3, 2],
                    [2, 1, 2]]


board_false_incorrect_number = [[1, 1, 0],
                                [1, 1, 2],
                                [2, 1, 2]]

board_win = [[2, 0, 1],
            [2, 1, 2],
            [2, 1, 2]]

board_no_win = [[2, 2, 1],
                [1, 1, 2],
                [2, 1, 2]]


def test_booling_return():
    assert type(tictactoe.validate_board(board=board_true)) is bool


def test_valid_board_true():
    assert tictactoe.validate_board(board=board_true) is True


def test_valid_board_false():
    assert tictactoe.validate_board(board=board_false) is False

def test_valid_board_false_2():
    assert tictactoe.validate_board(board=board_false_2) is False


def test_valid_board_incorrect_input():
    assert tictactoe.validate_board(board=booard_incorrect) is False


def test_valdi_board_incorrect_numbers():
    assert tictactoe.validate_board(board=board_false_incorrect_number) is False


def test_type_valid():
    assert type(tictactoe.game_finished(board=board_true)) is int

def test_game_continue():
    assert tictactoe.game_finished(board_true) == 0


def test_win_game():
    assert tictactoe.game_finished(board_win) == 1 or 2


def test_no_win():
    assert tictactoe.game_finished(board_no_win) == -1

def test_str_value():
    assert type(tictactoe.render_board(board_true)) is str






