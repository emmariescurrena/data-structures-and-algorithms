class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.prev = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.head == None:
            return "Empty stack"
        temp = self.head
        self.head = None
        self.head = temp.prev
        self.length -= 1
        return temp.data

    def peek(self):
        return self.head.data

    def __str__(self):
        if self.head == None:
            return "Empty stack"
        aux = Stack()
        current_node = self.head
        while current_node:
            aux.push(current_node.data)
            current_node = current_node.prev
        result = ""
        current_node = aux.head
        while current_node:
            result += f"{current_node.data}, "
            current_node = current_node.prev
        return result
