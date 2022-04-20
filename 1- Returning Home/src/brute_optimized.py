import sys

# Las nuevas entradas instant_x e instant_y tienen son pasados por las iteraciones anteriores
# para saber si es necesario recalcular o no las posiciones instantáneas en sus respectivos ejes
def solve(n, x, y, dest, instant_positions, board=None, instant_x=None, instant_y=None):
    if board is None:
        board = [[0] * n for _ in range(n)]

    if (x, y) == dest:
        return 0

    board[x][y] = 1

    result = sys.maxsize

    if instant_x is None:
        # Significa que la iteración anterior se desplazó por el eje y, y por tanto es necesario
        # recalcular las posiciones instantáneas por el eje x
        instant_x = search_for_instants_x(n, x, y, instant_positions)

    if instant_y is None:
        # Significa que la iteración anterior se desplazó por el eje x, y por tanto es necesario
        # recalcular las posiciones instantáneas por el eje y
        instant_y = search_for_instants_y(n, x, y, instant_positions)

    for pos in instant_x:
        _x, _y = pos

        if board[_x][_y] == 0:

            result = min(
                result, solve(n, _x, _y, dest, instant_positions, board, instant_x=[])
            )

    for pos in instant_y:
        _x, _y = pos

        if board[_x][_y] == 0:

            result = min(
                result, solve(n, _x, _y, dest, instant_positions, board, instant_y=[])
            )

    if y + 1 < n and board[x][y + 1] == 0:
        result = min(
            result,
            solve(n, x, y + 1, dest, instant_positions, board, instant_y=[]) + 1,
        )

    if y - 1 >= 0 and board[x][y - 1] == 0:
        result = min(
            result,
            solve(n, x, y - 1, dest, instant_positions, board, instant_y=[]) + 1,
        )

    if x + 1 < n and board[x + 1][y] == 0:
        result = min(
            result,
            solve(n, x + 1, y, dest, instant_positions, board, instant_x=[]) + 1,
        )

    if x - 1 >= 0 and board[x - 1][y] == 0:
        result = min(
            result,
            solve(n, x - 1, y, dest, instant_positions, board, instant_x=[]) + 1,
        )

    board[x][y] = 0
    return result


def search_for_instants_x(n, x, y, instant_positions):
    result = []

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


def search_for_instants_y(n, x, y, instant_positions):
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
    return result

