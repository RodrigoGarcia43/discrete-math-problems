import sys
import math


def analyze(n, x, y, dest, instant_positions, board=None):
    if board is None:
        temp = [0] * n
        board = []
        for _ in range(0, n):
            board.append(list.copy(temp))

    if (x, y) == dest:
        return 0

    board[x][y] = 1

    result = 100000000000000000000000000

    instants = search_for_instants(n, x, y, instant_positions)

    for pos in instants:
        _x, _y = pos

        if board[_x][_y] == 0:

            result = min(result, analyze(n, _x, _y, dest, instant_positions, board))

    if y + 1 < n and board[x][y + 1] == 0:
        result = min(result, analyze(n, x, y + 1, dest, instant_positions, board) + 1)

    if y - 1 >= 0 and board[x][y - 1] == 0:
        result = min(result, analyze(n, x, y - 1, dest, instant_positions, board) + 1)

    if x + 1 < n and board[x + 1][y] == 0:
        result = min(result, analyze(n, x + 1, y, dest, instant_positions, board) + 1)

    if x - 1 >= 0 and board[x - 1][y] == 0:
        result = min(result, analyze(n, x - 1, y, dest, instant_positions, board) + 1)

    board[x][y] = 0
    return result


def search_for_instants(n, x, y, instant_positions):
    result = []

    _y = y

    while _y <= n:
        _y += 1
        if (x, _y) in instant_positions:
            result.append((x, _y))

    _y = y

    while _y >= 0:
        _y -= 1
        if (x, _y) in instant_positions:
            result.append((x, _y))

    _x = x

    while _x <= n:
        _x += 1
        if (_x, y) in instant_positions:
            result.append((_x, y))

    _x = x

    while _x >= 0:
        _x -= 1
        if (_x, y) in instant_positions:
            result.append((_x, y))

    return result


def print_board(board, x, y):
    temp = board[x][y]
    board[x][y] = 2
    print("------------")
    for item in board:
        print(item)
    print("------------")
    board[x][y] = temp

