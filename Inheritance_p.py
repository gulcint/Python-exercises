# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:11:18 2019

@author: asus
"""

class Website(object):
    
        def __init__(self,name,surname):
            self.name = name
            self.surname = surname
            
        def logininfo(self):
            print(self.name + " " + self.surname)
            
            
class Website1(Website):
    
    #chid class
    def __init__(self,name,surname,ids):
        Website.__init__(self,name,surname)
        self.ids = ids
    
    def login(self):
        print(self.name + " " + self.surname +" " + self.ids)
    
    
class  Website2(Website):
    
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email = email
    
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
        
    
    
p1 = Website("gulcin","tas")
p2 = Website1("gulcin","tas","12255")
p3 = Website2("eren","duzulutas","eren@gmail.com")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        