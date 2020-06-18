from collections import defaultdict


class Graph:
    def __init__(self, no_of_nodes):
        self.graph = defaultdict(list)
        self.no_of_nodes = no_of_nodes

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, root):
        visited = [False]*nodes
        queue = [root]
        visited[root] = True

        while queue:
            root = queue.pop(0)
            print(root, end=" ")

            for el_adj_list in self.graph[root]:
                if not visited[el_adj_list]:
                    queue.append(el_adj_list)
                    visited[el_adj_list] = True


if __name__ == "__main__":
    nodes = int(input("No of nodes: "))
    g = Graph(no_of_nodes=nodes)
    n = int(input("Enter no of pairs to be entered: "))
    for i in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    root = int(input("Enter starting node: "))
    g.bfs(root)
