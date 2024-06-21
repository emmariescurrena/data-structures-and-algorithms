class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def pushNode(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def push(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        head = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        head.next = None
        return head.data

    def peek(self):
        return self.head.data

    def __str__(self):
        if self.head == None:
            return "Empty queue"
        result = ""
        current_node = self.head
        while current_node != None:
            result += f"{str(current_node.data)}, "
            current_node = current_node.next
        return result
