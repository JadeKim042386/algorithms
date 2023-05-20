class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0