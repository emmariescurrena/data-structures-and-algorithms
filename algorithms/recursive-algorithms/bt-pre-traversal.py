from tree import Node, Tree


def walk(curr, path):

    if curr is None:
        return

    path.append(curr.data)
    walk(curr.left, path)
    walk(curr.right, path)

    return path


tree = Tree()
tree.head = Node(1)
tree.head.left = Node(2)
tree.head.right = Node(5)
tree.head.left.left = Node(3)
tree.head.left.right = Node(4)
tree.head.right.left = Node(6)
tree.head.right.right = Node(7)

print(walk(tree.head, []))
