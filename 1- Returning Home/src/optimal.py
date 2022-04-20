import sys
from dijkstra import dijkstra

# Función principal
# Entradas:
# n -> Tamaño del tablero
# x, y  -> Coordenadas x y y de la posición inicial
# dest -> Tupla con las coordenadas x,y de la posición destino
# instant_position -> Lista de tuplas de coordenadas que representan las posiciones de desplazamiento instantáneo
def solve(n, m, initial_x, initial_y, dest, instant_positions):

    # Armando el grafo que tiene como nodos a la posición inicial y las posiciones instantáneas
    nodes = {}
    nodes[0] = (initial_x, initial_y)
    for index in range(1, m + 1):
        nodes[index] = instant_positions[index - 1]

    vertices = [[-1] * (m + 1) for _ in range(m + 1)]
    edges = [[-1] * (m + 1) for _ in range(m + 1)]

    # Ordenando las posiciones instantáneas por las x y por las y
    to_sort_by_x = []
    to_sort_by_y = []
    for key, pos in nodes.items():
        x, y = pos
        to_sort_by_x.append((x, y, key))
        to_sort_by_y.append((y, x, key))
    sorted_by_x = sorted(to_sort_by_x)
    sorted_by_y = sorted(to_sort_by_y)

    # Formando las aristas del grafo, con sus respectivos pesos
    for i in range(0, m):
        x, _, v = sorted_by_x[i]
        next_x, _, next_v = sorted_by_x[i + 1]

        vertices[v][next_v] = 1
        vertices[next_v][v] = 1

        new_distance = abs(x - next_x)

        if new_distance < edges[v][next_v] or edges[v][next_v] == -1:
            edges[v][next_v] = new_distance
            edges[next_v][v] = new_distance

        y, _, v = sorted_by_y[i]
        next_y, _, next_v = sorted_by_y[i + 1]

        vertices[v][next_v] = 1
        vertices[next_v][v] = 1

        new_distance = abs(y - next_y)

        if new_distance < edges[v][next_v] or edges[v][next_v] == -1:
            edges[v][next_v] = new_distance
            edges[next_v][v] = new_distance

    distances = dijkstra(vertices, edges)

    # La distancia pasando por el nodo i será igual a la distancia del inicio a ese nodo,
    # más la distancia del nodo al destino
    for i in range(0, len(distances)):
        distances[i] += abs(nodes[i][0] - dest[0]) + abs(nodes[i][1] - dest[1])

    # Se retorna la menor distancia
    return min(distances)

