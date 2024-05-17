class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def size(self):
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack.stack)
print("Popped item:", stack.pop())
print("Stack after pop:", stack.stack)
print("Top item:", stack.peek())
print("Stack size:", stack.size())
