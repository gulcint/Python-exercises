# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:11:59 2019

@author: asus
"""

# parent
class Animal:
    
    def __init__(self):
        print("Animal is created")
        
    def toString(self):
        print("animal")
    
    def walk(self):
        print("animal walk")
        
# child

class Monkey(Animal):        
    
    def __init__(self):
        super().__init__()
        print("Monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("Monkey can climb")
        
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def fly(self):
        print("fly")


        
m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()

print("-----")
 
b1 = Bird()
b1.walk()
b1.fly()



        
    
    
