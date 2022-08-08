
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
    
    ##add a access(self) function 

   