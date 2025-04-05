class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def appendleft(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node.next
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value
    
    def popleft(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value
    
    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.value))
            node = node.next
        return "[" +", ".join(result) + "]"