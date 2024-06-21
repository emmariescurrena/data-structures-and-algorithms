import numpy as np


mazes = [
    "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."]),

    "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...WW",
        "...W."]),

    "\n".join([
        "..W",
        ".W.",
        "W.."]),

    "\n".join([
        ".WWWW",
        ".W...",
        ".W.W.",
        ".W.W.",
        "...W."]),

    "\n".join([
        ".W...",
        "W....",
        ".....",
        ".....",
        "....."]),

    "\n".join([
        ".W",
        "W."])
]


def path_finder(maze):

    maze = maze.split()
    outWall = np.ones(len(maze)+2, dtype=int)
    ultMaze = [outWall]
    for i, r in enumerate(maze):
        ultMaze.append([1])
        i += 1
        for p in r:
            if p == 'W':
                ultMaze[i].append(1)
            else:
                ultMaze[i].append(0)
        ultMaze[i].append(1)
    ultMaze.append(outWall)

    ultMaze = np.array(ultMaze)

    def advance(maze, pY=1, pX=1, prev=2):

        maze[pY, pX] = 2

        if maze[-2, -2] == 2:
            return True

        positions = [[pY+1, pX, 2], [pY, pX+1, 3],
                     [pY-1, pX, 0], [pY, pX-1, 1]]
        del positions[prev]

        for pos in positions:
            slot = maze[pos[0], pos[1]]
            if slot == 0 and advance(maze, pos[0], pos[1], pos[2]) is True:
                return True

        return False

    return advance(ultMaze)


for m in mazes:
    print(path_finder(m))
