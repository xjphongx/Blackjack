

#testing class object
from audioop import avg
from statistics import mean


class placement():
    def __init__(self):
        self.left_bound = 0
        self.right_bound = 1000
        self.mid_point = average(self.right_bound, self.left_bound)




def average(num1, num2):
    average = (num1+num2)/2
    return average

    


#Testing below
p = placement()
print(p.mid_point)