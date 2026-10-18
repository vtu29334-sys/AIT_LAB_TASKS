from collections import deque

def disease_spread(n, roads, start_city):
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    queue = deque([(start_city, 0)])
    times = {start_city: 0}

    while queue:
        curr, time = queue.popleft()
        for neighbor in adj[curr]:
            if neighbor not in times:
                times[neighbor] = time + 1
                queue.append((neighbor, time + 1))
                
    return times
