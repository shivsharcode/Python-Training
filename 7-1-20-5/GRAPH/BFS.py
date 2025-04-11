from collections import deque  # double ended queue, operation can be done from both left and right


def bfs(graph, start):
    visited = set()
    queue = deque([start])  # enqueue the starting node
    # print(queue)
    while queue:
        node = queue.popleft()
        # print("POP")
        # print(queue)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process node
            queue.extend(graph[node]) # Add all unvisited neighbors
        # print(queue)


undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal")
# print(undirected_graph['B'])
bfs(undirected_graph, 'A')
