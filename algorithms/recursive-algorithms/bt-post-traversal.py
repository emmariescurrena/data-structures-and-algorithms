from tree import Node, Tree


def walk(curr, path):

    if curr is None:
        return

    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.data)

    return path


tree = Tree()
tree.head = Node(7)
tree.head.left = Node(3)
tree.head.right = Node(6)
tree.head.left.left = Node(1)
tree.head.left.right = Node(2)
tree.head.right.left = Node(4)
tree.head.right.right = Node(5)

print(walk(tree.head, []))
