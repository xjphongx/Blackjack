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
    def cut_deck(self):#cut the stack in half and place one half over another
        tempList = []

        ##40% - 60% cut so it cuts randomly
        print(f"40% {math.ceil(.4*self.size)}")
        print(f"60% {math.ceil(.6*self.size)}")
        cut_limit = random.randrange(math.ceil(.4*self.size),math.ceil(.6*self.size))
        print(f"Cut limit {cut_limit}")
        
        for i in range(cut_limit,self.size):
            tempList.append(self.stack[i])
        for j in range(0,cut_limit):
            tempList.append(self.stack[j])
          
        self.stack = tempList.copy()
        
    def casino_shuffle(self):
        tempList = [] #put upper half of object's stack into tempList
        #print(f"half {self.size/2} and full {self.size}")
        for i in range(int(self.size/2), self.size):
            tempList.append(self.stack[i])    
        for j in range(int(self.size/2), self.size):
            self.stack.pop()

        #Alternately shuffle the two list into a shuffled list
        shuffledList= []
        for k in range(int(self.size/2)):
            try:
                shuffledList.append(self.stack.pop(0))
                shuffledList.append(tempList.pop(0))
            except IndexError:
                print("Index error when casino shuffling")
                break
            
        self.stack = shuffledList[:]

        


   