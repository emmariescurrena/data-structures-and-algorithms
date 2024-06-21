from tree import Node, Tree


def search(curr, needle):

    if curr is None:
        return False

    if curr.data == needle:
        return True

    if curr.data < needle:
        return search(curr.right, needle)

    return search(curr.left, needle)


tree = Tree()
tree.head = Node(4)
tree.head.left = Node(2)
tree.head.right = Node(6)
tree.head.left.left = Node(1)
tree.head.left.right = Node(3)
tree.head.right.left = Node(5)
tree.head.right.right = Node(7)

print(search(tree.head, 1))
print(search(tree.head, 10))
print(search(tree.head, 6))
