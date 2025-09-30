def dfs(graph, start):
    visited = set()
    result = []

    def dfs_visit(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            dfs_visit(neighbor)

    dfs_visit(start)
    return result



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal starting from A:", dfs(graph, 'A'))
