
class Stack:
    ## predefined functions: append(),pop()
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def show(self):
        return self.stack
    
    ##add a access(self) function 

   