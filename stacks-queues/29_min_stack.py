class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val,self.min_stack[-1]))
        else:
            self.min_stack.append(val)    

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

obj = MinStack()
obj.push(5)
obj.push(6)
obj.push(2)
obj.push(4)
obj.push(1)
print(obj.pop())
print(obj.getMin())