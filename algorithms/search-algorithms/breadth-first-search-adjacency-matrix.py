def search(graph, needle, seen, prev):
    while len(queue):
        curr = queue.pop(0)
        if curr == needle:
            break
        adjs = graph[curr]
        for i in range(len(adjs)):
            if adjs[i] == 0 or seen[i] == True:
                continue
            seen[i] = True
            prev[i] = curr
            queue.append(i)
        seen[curr] = True

    curr = needle
    out = []

    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]
    if len(out):
        out.append(curr)
        return list(reversed(out))
    return []


graph = [
    [False, True, False, False],
    [False, False, True, False],
    [True, False, False, False],
    [True, False, True, False],
]

source = 0
needle = 0
seen = [False for i in range(len(graph))]
seen[source] = True
prev = [-1 for i in range(len(graph))]
queue = [source]

print(search(graph, needle, seen, prev))
