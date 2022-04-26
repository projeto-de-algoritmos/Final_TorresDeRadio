def greedyColoring(adj, V):
    result = [-1] * V

    result[0] = 0

    available = [False] * V

    for u in range(1, V):

        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = True

        color = 0
        while color < V:
            if (available[color] == False):
                break

            color += 1

        result[u] = color

        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False

    dict = {}

    for u in range(V):
        print("Nó", u, "Cor", result[u])
        dict[int(u)] = result[int(u)]
    return dict

def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)
    return adj



