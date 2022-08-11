import random
import math

class Stack:
    ## predefined functions: append(),pop()
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def show(self):
        return self.stack
    
    def get_size(self): #return length of the list
        return len(self.stack)
    
    def update_size(self): #update should be used once
        self.size = len(self.stack)

    def cut(self):#cut the stack in half and place one half over another
        #print(f"Full stack size before cut {self.size}")
        tempList = []

        ##40% - 60% cut so it cuts randomly
        print(f"40% {math.ceil(.4*self.size)}")
        print(f"60% {math.ceil(.6*self.size)}")
        cut_limit = random.randrange(math.ceil(.4*self.size),math.ceil(.6*self.size))
        print(f"Cut limit {cut_limit}")
        
        for i in range(cut_limit,self.size):
            #print(f"Value taken out {self.stack[i]}")
            #tempList.append(i)
            tempList.append(self.stack[i])


        for j in range(0,cut_limit):
            tempList.append(self.stack[j])
            #tempList.append(j)

        self.stack = tempList.copy()
        
        
        
        




    
    ##add a access(self) function 

   