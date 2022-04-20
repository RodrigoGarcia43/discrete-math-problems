from utils import Tree


# Función principal
# Entradas:
# n -> Cantidad de vértices de S
# s_edges  -> Aristas de S
# m -> Cantidad de vértices de T
# t_edges-> Aristas de T
def solve(n, s_edges, m, t_edges):
    # Se forman los árboles y se enraíza S en un punto arbitrario.
    S = Tree(n, s_edges)
    T = Tree(m, t_edges)
    S.make_root(0)
    mod = 1e9 + 7

    ans1 = 0

    for i in range(m):
        # Para cada vértice i de T, se enraiza a T en i y se calcula las respuestas para ese rooted tree.
        visited = [[] for _ in range(n)]
        dp = [{} for _ in range(n)]
        T.make_root(i)
        for j in range(n):
            ans1 += (
                calculate(j, len(S.sons[j]) - 1, T.bitmask[i], S, T, visited, dp, mod)
                % mod
            )

    # Calculando cantidad de automorfismos de S.
    ans2 = 0
    S = Tree(m, t_edges)
    S.make_root(0)
    for i in range(m):
        visited = [[] for _ in range(n)]
        dp = [{} for _ in range(n)]
        T.make_root(i)
        ans2 += (
            calculate(0, len(S.sons[0]) - 1, T.bitmask[i], S, T, visited, dp, mod) % mod
        )

    result = int(ans1 / ans2)
    return result


# Función para calcular la cantidad de subtrees de S, con raíz en v, que son isomorfos con T.
def calculate(v, son, bits, S, T, visited, dp, mod):
    # Caso base que se alcanza cuando se ha analizado a todos los hijos de v.
    # Si no quedan bits con valor 1, es un matcheo positivo.
    if son == -1:
        result = 1
        for b in bits:
            if b == 1:
                result = 0
                break
        return result

    u = S.sons[v][son]

    # Si el hijo u, con los actuales bits, ya fue calculado, se retorna el valor almacenado.
    if str(bits) in visited[u]:
        return dp[u][str(bits)]

    visited[u].append(str(bits))

    # Calculando la respuesta sin tener en cuenta a u.
    result = calculate(v, son - 1, bits, S, T, visited, dp, mod)

    for i in range(T.n):
        if bits[i] == 1:
            # Se matchea a u con i.
            bits[i] = 0
            same_level = calculate(v, son - 1, bits, S, T, visited, dp, mod)
            bits[i] = 1
            deep_level = calculate(
                u, len(S.sons[u]) - 1, T.bitmask[i], S, T, visited, dp, mod
            )

            mult = same_level * deep_level % mod
            result = (result + mult) % mod

    dp[u][str(bits)] = result
    return result
