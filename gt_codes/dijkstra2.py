def minDist(mdist, vset, V):
    minVal = float('inf')
    minInd = -1
    for i in range(V):
        if (not vset[i]) and mdist[i] < minVal:
            minVal = mdist[i]
            minInd = i
    return minInd

def dijkstra2(graph, V, src):
    mdist = [float('inf')] * V
    vset = [False] * V
    mdist[src] = 0

    for i in range(V - 1):
        u = minDist(mdist, vset, V)
        vset[u] = True

        for v in range(V):
            if (not vset[v]) and graph[u][v] != float('inf') and mdist[u] + graph[u][v] < mdist[v]:
                mdist[v] = mdist[u] + graph[u][v]

if __name__ == "__main__":
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter shortest path source:").strip())
    dijkstra2(graph, V, gsrc)