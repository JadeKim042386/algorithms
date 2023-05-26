def BellmanFord(graph, V, E, src):
    mdist = [float('inf') for i in range(V)]
    mdist[src] = 0.0

    for i in range(V - 1):
        for j in range(E):
            u = graph[j]['src']
            v = graph[j]['dst']
            w = graph[j]['weight']

            if mdist[u] != float('inf') and mdist[u] + w < mdist[v]:
                mdist[v] = mdist[u] + w
    
    for j in range(E):
        u = graph[j]['src']
        v = graph[j]['dst']
        w = graph[j]['weight']

        if mdist[u] != float('inf') and mdist[u] + w < mdist[v]:
            return
    
    return src
