from stack import Stack


def walk(graph, needle, seen, path, curr):
    if seen[curr]:
        return False

    path.push(curr)
    if curr == needle:
        print(path)
        return True

    seen[curr] = True
    list = graph[curr]
    for i in list:
        if walk(graph, needle, seen, path, i):
            return True

    path.pop()
    return False


graph = [
    [1],
    [2],
    [0],
    [1, 2],
]
needle = 2
source = 0
seen = [False for i in range(len(graph))]
path = Stack()

print(walk(graph, needle, seen, path, source))
