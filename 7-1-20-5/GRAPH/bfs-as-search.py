from collections import deque


def bfs_shortest_path(graph, start, target):
    visited = set()
    queue = deque( [ (start, [start]) ] )
    print(queue)
    while queue:
        node, path = queue.popleft()
        print("POP")
        print(queue)
        if node == target:
            return path  # Return the shortest path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))  # path + [neighbor] creates a new list
                print("Append")
                print(queue)

undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Shortest Path from A to F : ")
shortest_path_A_F = bfs_shortest_path(undirected_graph, 'A', 'F')
print(shortest_path_A_F)
# start = 'A'
# q = deque([(start, [start])])
# print(q.popleft())