class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)

# tests

s = Stack()

print(s.isEmpty())      # true
s.push(4)
s.push(1)
s.push(3)
print(s.isEmpty())      # false
print(s.size())         # 3
s.printStack()          # [4, 1, 3]
s.pop()
s.printStack()          # [4, 1]
print(s.peek())         # 1
