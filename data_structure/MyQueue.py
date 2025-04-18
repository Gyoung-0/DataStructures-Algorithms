class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("값이 비어있습니다")
        value = self.queue[0]
        self.queue = self.queue[1:]
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("값이 비어있습니다")
        return self.queue[0]


    def is_empty(self):
        return len(self.queue) == 0

q = MyQueue()

print("is_empty?", q.is_empty())  # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("peek:", q.peek())  # 10
print("dequeue:", q.dequeue())  # 10
print("peek:", q.peek())  # 20
print("dequeue:", q.dequeue())  # 20

q.enqueue(40)
print("peek:", q.peek())  # 30
print("dequeue:", q.dequeue())  # 30
print("dequeue:", q.dequeue())  # 40

print("is_empty?", q.is_empty())  # True

# 예외 확인
try:
    q.dequeue()
except IndexError as e:
    print("예외 발생:", e)