from print_tree import print_tree


class Node:
    def __init__(self, idx, parent):
        self.id = idx
        self.parent = parent
        self.children = []
        self.rooted_subtrees = []

    def __str__(self):
        return str(self.id)

    def copy(self):
        result = Node(self.id, self.parent)
        result.children = self.children.copy()
        result.rooted_subtrees = self.rooted_subtrees.copy()
        return result


class Print_tree(print_tree):
    def get_children(self, node):
        return node.children

    def get_node_str(self, node):
        return str(node.id)


class Tree:
    def __init__(self, n, edges):
        self.n = n
        self.edges = [[0] * n for _ in range(n)]
        self.degrees = [0] * n
        for u, v in edges:
            u, v = u - 1, v - 1
            self.edges[v][u] = 1
            self.edges[u][v] = 1
            self.degrees[u] += 1
            self.degrees[v] += 1

        self.sons = [[] for _ in range(n)]
        self.bitmask = [[0] * n for _ in range(n)]

    def make_root(self, root, father=-1):
        self.sons[root] = []
        self.bitmask[root] = [0] * self.n
        for i in range(self.n):
            if self.edges[root][i] == 1 and i != father:
                self.sons[root].append(i)
                self.make_root(i, root)
                self.bitmask[root][i] = 1

    def get_center(self):
        n = self.n
        while True:
            to_reduce = []
            for i in range(self.n):
                if self.degrees[i] == 1:
                    self.degrees[i] -= 1
                    n -= 1
                    for j in range(self.n):
                        if self.edges[i][j] == 1 and self.degrees[j] > 0:
                            to_reduce.append(j)
                            break

            if n <= 2:
                break
            for item in to_reduce:
                self.degrees[item] -= 1

        for i in range(self.n):
            if self.degrees[i] > 0:
                return i
