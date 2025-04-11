
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" "),
            visited.add(node)
            stack.extend(reversed(graph[node]))

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E', 'C']
}

print("DFS Iterative Traversal")
dfs_iterative(graph, 'A')


