# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:09:51 2019

@author: asus
"""

class Animal(object):
    
    def toString(self):
        print("Animal")
        

class Monkey(Animal):
    
    def toString(self):
        print("Monkey")
    
#a1 = Animal()
#a1.toString()

m1 = Monkey()
m1.toString()