class Node:
    def __init__(self, key, value):
        self.value = value
        self.next = None
        self.prev = None


class LRU:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.capacity = 10
        self.lookup = map(key, Node())
        self.reverse_lookup = map(Node(), key)

    def update(self, key, value):

        node = self.lookup(key)

        self.length += 1

    def get(self, key):
        node = self.lookup(key)

        self.key.prev.next = self.key.next
        self.key.next.prev = self.key.prev
        self.key.next = self.head
        self.head.prev = self.key
        self.head = self.key

        return self.key.value
