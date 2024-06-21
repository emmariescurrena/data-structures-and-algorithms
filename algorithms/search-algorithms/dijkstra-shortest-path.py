def hasUnvisited(seen, dists):
    for i in range(len(seen)):
        if seen[i] is False and dists[i] < float("inf"):
            return True
    return False


def getLowestUnvisited(seen, dists):
    lo = -1
    lowest_distance = float("inf")

    for i, dist in enumerate(dists):
        if seen[i]:
            continue
        if dist < lowest_distance:
            lowest_distance = dist
            lo = i
    return lo


def dijkstra(graph, dists):
    while hasUnvisited(seen, dists):
        lo = getLowestUnvisited(seen, dists)
        seen[lo] = True
        for edge in graph[lo]:
            i = edge["to"]
            if seen[i]:
                continue
            dist = dists[lo] + edge["dist"]
            if dist < dists[i]:
                dists[i] = dist
                prev[i] = lo
    return dists


graph = [
    [{"to": 1, "dist": 4},
     {"to": 2, "dist": 2},],
    [{"to": 0, "dist": 2},
     {"to": 2, "dist": 5},
     {"to": 3, "dist": 3},],
    [{"to": 0, "dist": 4},
     {"to": 1, "dist": 5},
     {"to": 4, "dist": 2},],
    [{"to": 1, "dist": 3},
     {"to": 4, "dist": 1},],
    [{"to": 2, "dist": 2},
     {"to": 3, "dist": 1},]
]

source = 0
seen = [False for i in range(len(graph))]
dists = [float("inf") for i in range(len(graph))]
prev = [-1 for i in range(len(graph))]
dists[source] = 0

print(dijkstra(graph, dists))
