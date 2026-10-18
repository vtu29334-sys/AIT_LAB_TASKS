def valid(g, c, v, col):
    return all(col.get(i) != c for i in g[v])

def solve(g, c, nodes, idx=0, col={}):
    if idx == len(nodes): return col
    v = nodes[idx]
    for color in c:
        if valid(g, color, v, col):
            col[v] = color
            res = solve(g, c, nodes, idx + 1, col)
            if res: return res
            del col[v]
    return None

graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}
colors = [1, 2, 3]
print(solve(graph, colors, list(graph.keys())))
