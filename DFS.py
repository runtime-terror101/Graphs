from collections import defaultdict


class Graph:
    def __init__(self, no_of_nodes):
        self.graph = defaultdict(list)
        self.no_of_nodes = no_of_nodes

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recurse(self, visited, root):
        visited[root] = True
        print(root, end=" ")
        for adj_el in self.graph[root]:
            if not visited[adj_el]:
                self.dfs_recurse(visited, adj_el)

    def dfs(self, root):
        visited = [False] * self.no_of_nodes
        self.dfs_recurse(visited, root)


if __name__ == "__main__":
    nodes = int(input("No of nodes: "))
    g = Graph(no_of_nodes=nodes)
    n = int(input("Enter no of pairs to be entered: "))
    for i in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    root = int(input("Enter starting node: "))
    g.dfs(root)

