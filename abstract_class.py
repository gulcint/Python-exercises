# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:09:46 2019

@author: asus
"""

from abc import ABC, abstractmethod

class Animal(ABC) : # super class , Animal class Abstract class haline geldi.
    @abstractmethod
    def walk(self): pass
    @abstractmethod
    def run(self): pass
    


class Bird(Animal): # sub class
    
    def __init__(self):
        print("bird")
        
    def walk(self): 
        print("walk")

    def run(self):
        print("walk")
    

b1 = Bird()
b1.run()