"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
"""

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

stack = MyStack()
print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())
print(stack.pop())
print(stack.empty())
stack.display()

