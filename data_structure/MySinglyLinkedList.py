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
        
        

    def reverse(self):
        if self.head == None:
            raise ValueError("list in empty")
        
        # 1. 이전 노드, 현재 노드, 다음 노드
        prev =  None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def to_list(self):
        if self.head == None:
            return []
        
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next

        return result
    
def merge_list(node1, node2):
    dummy = Node(0)
    tail = dummy

    while node1 and node2:
        if node1.value <= node2.value:
            tail.next = node1
            node1 = node1.next
        else:
            tail.next = node2
            node2 = node2.next
        tail = tail.next

    if node1:
        tail.next = node1
    else:
        tail.next = node2
    
    return dummy.next

