class Stack:
    def __init__(self):
        super().__init__()
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        some_list = []
        "[{element(N)}, {element(N-1)} ... {element(0)}]"
        for idx in range(len(self.data) - 1, -1, -1):
            some_list.append(self.data[idx])
        return f"[{', '.join(some_list)}]"

stack = Stack()
stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
print(stack)
