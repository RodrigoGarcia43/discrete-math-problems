import sys

# Función principal
# Entradas:
# n -> Tamaño del tablero
# x, y  -> Coordenadas x y y de la posición inicial
# dest -> Tupla con las coordenadas x,y de la posición destino
# instant_position -> Lista de tuplas de coordenadas que representan las posiciones de desplazamiento instantáneo
# board -> tablero armado en la primera iteración
def solve(n, x, y, dest, instant_positions, board=None):
    if board is None:
        board = [[0] * n for _ in range(n)]

    # Caso base, se llega al destino
    if (x, y) == dest:
        return 0

    board[x][y] = 1

    result = sys.maxsize

    # Se busca las posiciones instantáneas por las 4 direcciones
    instants = search_for_instants(n, x, y, instant_positions)

    for pos in instants:
        _x, _y = pos

        if board[_x][_y] == 0:
            # Se calcula la solución en caso de moverse hacia las posiciones instantáneas
            result = min(result, solve(n, _x, _y, dest, instant_positions, board))

    # Se calcula la solución en caso de dar un paso en cada dirección
    if y + 1 < n and board[x][y + 1] == 0:
        result = min(result, solve(n, x, y + 1, dest, instant_positions, board) + 1)
    if y - 1 >= 0 and board[x][y - 1] == 0:
        result = min(result, solve(n, x, y - 1, dest, instant_positions, board) + 1)
    if x + 1 < n and board[x + 1][y] == 0:
        result = min(result, solve(n, x + 1, y, dest, instant_positions, board) + 1)
    if x - 1 >= 0 and board[x - 1][y] == 0:
        result = min(result, solve(n, x - 1, y, dest, instant_positions, board) + 1)

    board[x][y] = 0
    return result


# Función auxiliar para buscar posiciones instantáneas
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

