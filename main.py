#get output with the sets first DONE
from tkinter import *


class Set:
    arr = []
    i = 0

    def __init__(self, num):
        self.num = num
    
    def generate_set(self,num):
        
        if Set.i == 0:
            print(self.arr)
            Set.i+=1

        for i in range(num+1):
            Set.arr.append(i)
            i+=1 
            print(self.arr)
        
    #def generate_square(self, num):

p1 = Set(2)
p1.generate_set(2)
