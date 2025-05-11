class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("값이 비어있습니다")
        return self.queue.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("값이 비어있습니다")
        return self.queue[0]


    def is_empty(self):
        return len(self.queue) == 0
    
    class Queue:
        def __init__(self):
            self.queue = []
        def enqueue(self, value):
            self.queue.append(value)
        def dequeue(self):
            if self.is_empty():
                raise IndexError("값이 비었습니다")
            value