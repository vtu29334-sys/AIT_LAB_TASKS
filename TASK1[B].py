 def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Input
n = int(input("Enter number of vertices: "))
graph = {}

for _ in range(n):
    data = list(map(int, input().split()))
    graph[data[0]] = data[1:]

start = int(input("Enter starting vertex: "))

# DFS
visited = set()
dfs(graph, start, visited)

# Output
print("{" + ",".join(map(str, sorted(visited))) + "}")
