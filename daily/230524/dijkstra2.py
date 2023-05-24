def minDist(mdist, visited, V):
    minVal = float('inf')
    minIdx = -1
    for i in range(V):
        if (not visited[i]) and mdist[i] < minVal:
            minVal = mdist[i]
            minIdx = i
    return minIdx

def dijkstra2(graph, V, src):
    mdist = [float('inf')] * V
    visited = [False] * V
    mdist[src] = 0

    for _ in range(V - 1):
        u = minDist(mdist, visited, V)
        visited[u] = True

        for v in range(V):
            if (not visited[v]) and graph[u][v] != float('inf') and mdist[u] + graph[u] < mdist[v]:
                mdist[v] = mdist[u] + graph[u][v]
