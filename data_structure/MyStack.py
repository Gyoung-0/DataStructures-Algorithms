class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty() :
            raise IndexError("스택이 비어있습니다.")
        stack_value = self.stack[-1]
        del self.stack[-1] # pop안쓰고 해보기
        return stack_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("스택이 비어있습니다")
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    s = MyStack()
    print("스택이 비었나요?", s.is_empty())  # ➜ True

    s.push(10)
    s.push(20)
    s.push(30)

    print("현재 top 값:", s.peek())         # ➜ 30
    print("pop:", s.pop())                 # ➜ 30
    print("pop:", s.pop())                 # ➜ 20
    print("현재 top 값:", s.peek())         # ➜ 10
    print("스택이 비었나요?", s.is_empty())  # ➜ False

    print("pop:", s.pop())                 # ➜ 10
    print("스택이 비었나요?", s.is_empty())  # ➜ True

    # 비어있는 스택에서 pop 시도 → 예외 발생
    s.pop()