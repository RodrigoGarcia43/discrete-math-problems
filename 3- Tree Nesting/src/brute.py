from utils import Node, Print_tree, Tree
import itertools

# Función principal
# Entradas:
# n -> Cantidad de vértices de S
# s_edges  -> Aristas de S
# m -> Cantidad de vértices de T
# t_edges-> Aristas de T
def solve(n, s_edges, m, t_edges):
    # Creando y enraizando a S y a T.
    S = Tree(n, s_edges)
    T = Tree(m, t_edges)
    S.make_root(0)
    T.make_root(0)

    center = S.get_center()
    S.make_root(center)

    # Se obtienen todos los subtrees de S.
    subtrees = []
    for i in range(n):
        # Obteniendo subtrees de S cuya raíz es i.
        subtrees += get_rooted_subtrees(S, i)[0]

    mask = [0] * (len(subtrees))

    for i in range(m):
        T.make_root(i)
        t = convert(T, i)
        for j in range(len(subtrees)):
            # Si el subtree j es isomorfo con T y esto no se sabía todavía, se marca como sabido.
            if mask[j] == 0 and check_if_isomorphic(subtrees[j], t):
                mask[j] = 1

    result = 0
    for item in mask:
        result += item

    return result


# Función para convertir un Tree en una forma más sencilla, Node.
# El Node tendrá como hijos a otros objetos de tipo Node y facilitará la recursión.
def convert(tree, root, father=-1):
    result = Node(root, father)
    for son in tree.sons[root]:
        result.children.append(convert(tree, son, root))
    return result


# Función para obtener todos los subtrees enraizados en un vértice dado.
def get_rooted_subtrees(tree, actual, father=-1):
    if len(tree.sons[actual]) == 0:
        return [[Node(actual, father)]]

    children_rooted_subtrees = []

    # Se busca recursivamente los subtrees de los hijos.
    for son in tree.sons[actual]:
        children_rooted_subtrees += get_rooted_subtrees(tree, son, actual)

    result = []
    # Se hacen combinaciones de los hijos de todos los tamaños posibles y se une los rooted subtrees de estos
    # de todas las formas posibles, empatándolos con la nueva raíz que es el vértice actual.
    for k in range(len(children_rooted_subtrees) + 1):
        combinations = list(itertools.combinations(children_rooted_subtrees, k))
        for comb in combinations:
            if len(comb) == 0:
                result += [Node(actual, father)]
            else:
                result += mix_rooted_subtrees(comb, actual, father)

    return [result]


# Función utilizada para unir subtrees de una combinación de hijos.
# Comb es una lista de listas de rooted subtrees.
# Se forman nuevos subtrees con idx como raíz.
def mix_rooted_subtrees(comb, idx, father, index=0):

    if index == len(comb) - 1:
        result = []
        for t in comb[index]:
            newNode = Node(idx, father)
            newT = t.copy()
            newT.parent = newNode
            newNode.children.append(newT)
            result.append(newNode)
        return result

    result = []
    for tree in mix_rooted_subtrees(comb, idx, father, index + 1):
        for t in comb[index]:
            newTree = tree.copy()
            newTree.children.append(t)
            result.append(newTree)
    return result


# Función para verificar si dos ároles a y b son o no isomorfos.
def check_if_isomorphic(a, b):
    # Si ambos son hojas, son isomorfos
    if len(a.children) == 0 and len(b.children) == 0:
        return True

    # Si no tienen igual cantidad de hijos, no son isomorfos.
    if len(a.children) != len(b.children):

        return False

    b_per = list(itertools.permutations(b.children))

    result = False
    for per in b_per:
        for i in range(len(a.children)):
            if not check_if_isomorphic(per[i], a.children[i]):
                result = False
                break

            result = True

        # Si hay una combinación de los hijos de b tal que todo hijo per de b sea isomorfo con el hijo i de a,
        # entonces son isomorfos.
        if result:
            return True

    # Al no tener ninguna permutación favorable, se retorna falso.
    return False

