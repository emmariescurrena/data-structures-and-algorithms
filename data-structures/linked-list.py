class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(new_node)
            return
        while current_node != None and position+1 != index:
            position += 1
            current_node = current_node.next
        if current_node is None:
            print("Index doesn't exist")
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self, value, index):
        current_node = self.head
        position = 0
        while position != index and current_node != None:
            position += 1
            current_node = current_node.next
        if current_node is None:
            print("Index doesn't exist")
        else:
            current_node.data = value

    def removeFirstNode(self):
        if self.head is None:
            print("Empty linked list")
            return
        self.head = self.head.next

    def removeLastNode(self):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def removeAtIndex(self, index):
        if self.head is None:
            print("Empty linked list")
            return
        if index == 0:
            self.removeFirstNode()
            return
        current_node = self.head
        position = 0
        while position+1 != index and current_node != None:
            position += 1
            current_node = current_node.next
        if current_node is None or current_node.next is None:
            print("Index doesn't exist")
        else:
            current_node.next = current_node.next.next

    def removeValue(self, value):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node != None and current_node.next.data != value:
            current_node = current_node.next
        if current_node is None:
            print("Value was not founded")
        else:
            current_node.next = current_node.next.next

    def length(self):
        if self.head is None:
            return 0
        current_node = self.head.next
        length = 1
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def insertArrElementsAtEnd(self, arr):
        if self.head is None:
            self.head = Node(arr.pop(0))
            current_node = self.head
            for i in arr:
                current_node.next = Node(i)
                current_node = current_node.next
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        for i in arr:
            current_node.next = Node(i)
            current_node = current_node.next

    def __str__(self):
        if self.head == None:
            return "Empty linked list"
        result = ""
        current_node = self.head
        while current_node != None:
            result += f"{str(current_node.data)}, "
            current_node = current_node.next
        return result

# Problem 1: Convert singly listed link to circular linked list
# and check if linked list is circular


def singlyToCircular(list):
    if list.head is None:
        print("Empty linked list")
        return
    current_node = list.head
    while current_node.next:
        current_node = current_node.next
    current_node.next = list.head


def isCircular(head):
    if head is None:
        return True
    current_node = head
    while current_node != head and current_node != None:
        current_node = current_node.next
    return (current_node == head)

# Problem 2: Detect loop in a linked list


def detectLoop(head):
    current_node = head
    seen_nodes = set()
    while current_node:
        if current_node in seen_nodes:
            return True
        seen_nodes.add(current_node)
        current_node = current_node.next
    return False


# Problem 3: Find intersection of two linked lists

linkedList1 = LinkedList()
linkedList2 = LinkedList()
linkedList1.insertArrElementsAtEnd([4, 8, 5, 9])
linkedList2.insertArrElementsAtEnd([3, 2])
linkedList2.head.next.next = linkedList1.head.next


def startPositionBigList(head, difference):
    current_node = head
    while difference > 0:
        current_node = current_node.next
        difference -= 1
    return current_node


def detectIntersection(list1, list2):
    list1_len = list1.length()
    list2_len = list2.length()

    if list1_len > list2_len:
        difference = list1_len - list2_len
        list1_current_node = startPositionBigList(list1.head, difference)
        list2_current_node = list2.head

    elif list2_len > list1_len:
        difference = list2_len - list1_len
        list1_current_node = list1.head
        list2_current_node = startPositionBigList(list2.head, difference)

    else:
        list1_current_node = list1.head
        list2_current_node = list2.head

    while True:
        if list1_current_node == list2_current_node:
            return list1_current_node.data
        list1_current_node = list1_current_node.next
        list2_current_node = list2_current_node.next

# Source: https://www.geeksforgeeks.org/data-structures/linked-list/
