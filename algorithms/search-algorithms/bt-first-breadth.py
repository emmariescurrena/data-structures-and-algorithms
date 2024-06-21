from tree import Node, Tree


def valueInTree(curr, needle):

    queue = [curr]
    while len(queue) > 0:
        curr = queue.pop(0)

        if curr.data == needle:
            return True

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return False


tree = Tree()
tree.head = Node(1)
tree.head.left = Node(2)
tree.head.right = Node(3)
tree.head.left.left = Node(4)
tree.head.left.right = Node(5)
tree.head.right.left = Node(6)
tree.head.right.right = Node(7)

print(valueInTree(tree.head, 8))
