class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0:
            raise ValueError("인덱스는 양수로 입력해주세요")
        if self.list_count() < index:
            raise IndexError("리스트의 최대 길이보다 인덱스가 큽니다.")
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        new_node = Node(value)
        count = 0
        current = self.head
        while count != index:
            count += 1
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def list_count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def delete(self, index):
        if index < 0:
            raise ValueError("Index is higher than zero")
        if self.head is None:
            raise IndexError("none of deleting data")
        if index >= self.list_count():
            raise IndexError("Index is excessive range of list") 
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        
        count = 0
        
        while count != index-1:
            current = current.next
            count += 1
            
        current.next = current.next.next
        
    def get(self, index):
        if index < 0:
            raise ValueError("index is higher than 0")
        if self.head is None:
            raise IndexError("list in empty")
        if self.list_count() <= index:
            raise ValueError("index is lower than maximum length of list")
        
        current = self.head
        count = 0
        while count != index:
            current = current.next
            count += 1
        return current.value
        
        