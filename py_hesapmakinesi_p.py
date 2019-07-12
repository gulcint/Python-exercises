# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 22:57:20 2019

@author: asus
"""

class Calc(object):
    
    # init metedou
    def __init__(self,a,b):
      
      # attiribute
      self.value1 = a
      self.value2 = b
      
    
    def add(self):  
        
        return self.value1 + self.value2
      
      
    def multiply(self):
        
        return self.value1 * self.value2
      
    def division(self):
        
        return (float( self.value1 / self.value2))
      
      
print("Choose add(1), multiply(2), division(3)")
selection = input("select 1 or 2 or 3")

v1 = int( input("first value"))
v2 = int( input("second value"))


c1 = Calc(v1,v2)

if selection == "1" :
    add_result = c1.add()
    print("add",add_result)
elif selection == "2" :
    multiply_result = c1.multiply()
    print("Multiply : ", multiply_result)
elif selection == "3" :
    division_result =c1.division()
    print("Division :" , division_result)
    


