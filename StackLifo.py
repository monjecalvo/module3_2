class StackLifo():
    
    def __init__(self):
        self.mystack = []

    def push(self,element):
        self.mystack.append(element)    

    def pop(self):
        if len(self.mystack) > 0:
            return self.mystack.pop()
        return None
stack = StackLifo()

stack.push(5)

stack.push(7)

print(stack.pop())
print(stack.pop())