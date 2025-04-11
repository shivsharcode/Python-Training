def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)  # Mark as visited
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)


# Example Graph (Adjacency List)
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

weighted_graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 3), ('E', 1)],
    'C': [('A', 5), ('F', 6)],
    'D': [('B', 3)],
    'E': [('B', 1), ('F', 8)],
    'F': [('C', 5), ('E', 8)]
}

visited_set = set()
print("DFS Recursive Traversal: ")
dfs_recursive(undirected_graph, 'A', visited_set)
