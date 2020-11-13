def validate_board(board):
    zero_number = 0
    first_pl = 0
    second_pl = 0
    if len(board) == 3:
        for line in board:
            if len(line) == 3:
                for number in line:
                    if number == 0:
                        zero_number += 1
                    elif number == 1:
                        first_pl += 1
                    elif number == 2:
                        second_pl += 1
                    else:
                        return False
            else:
                return False
        if first_pl == second_pl or first_pl - second_pl == 1 or second_pl - first_pl == 1:
            return True
        else:
            return False
    else:
        return False


def game_finished(board):
    null_count = 0
    for line in board:
        if line[0] == line[1] == line[2] and 0 not in line:
            return line[0]
        elif 0 in line:
            null_count += 1
    win_column = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]]
                  ]
    for colum in win_column:
        if colum[0] == colum[1] == colum[2] and 0 not in colum:
            return colum[0]
    win_strike = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for strike in win_strike:
        if strike[0] == strike[1] == strike[2] and 0 not in strike:
            return strike[0]
    if null_count > 0:
        return 0
    else:
        return -1


def render_board(board):
    head = f"""<head>
                    <meta charset="UTF-8">
                    <title>Крестики нолики</title>
                    </head>"""
    body = f"""<h1>Ваш ход</h1>"""
    field = ""
    for line in board:
        field += f"""<tr>"""
        for i in line:
            item = ""
            if i == 1:
                item = f"""<td>X</td>"""
            elif i == 2:
                item = f"""<td>O</td>"""
            else:
                item = f"""<td>&nbsp;</td>"""
            field += item
        field += "</tr>"


    page = f"""<!DOCTYPE html>
                    <html lang="en">
                    {head}  
                    {body}
                    <table>
                        {field}
                    </table>
                </html>"""
    return page


board = [
    [1, 2, 0],
    [1, 0, 2],
    [2, 1, 2]
]


render_board(board)



