# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:01:40 2019

@author: asus
"""

class Employee :
     
     def raisee(self):
         raise_rate = 0.1
         result = 100 +100* raise_rate
         print("E : ", result)
     
     
class ComEng(Employee):
    
    def raisee(self):
         raise_rate = 0.2
         result = 100 +100* raise_rate
         print("CE : ", result)
     
     
class EEE(Employee):
    
    def raisee(self):
         raise_rate = 0.3
         result = 100 +100* raise_rate
         print("EEE : ", result)
     
e1 = Employee()

ce = ComEng()

eee = EEE()
     

employee_list = [ce,eee]

for employee in employee_list:
    employee.raisee()


    
         