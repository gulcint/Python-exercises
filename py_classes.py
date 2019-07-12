# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:37:55 2019

@author: asus
"""

# %%
integer1 = 33
string1 = "messi" 

#%% classes

employee1_name = "messi"
employee1_age = 33
employee_address = "mimarsinan .."


class Employee:
  """ attribute (age,addess,name)
      behaviour (run,swim)
  """
  pass

""" classtan nesne türetirken """
employee1 = Employee()

#%%  attribute

class Footballer:
  
  football_clup = "barca"
  age = 30
    
f1 = Footballer()

print(f1)
print(f1.age)
print(f1.football_clup)

f1.football_clup = "Real Madrid"

#%% methods

class Square(object):
    
  edge = 5 #meter
  area = 0
  
  def area1(self):
  
    self.area = self.edge* self.edge  #self kullanılmayınca edge variable ni görmüyor.
    # self ile objene ait , classına ait variableleri kullanacıksın demektir
    
    print("Area:",self.area)
    
    
s1 = Square()

print(s1.area1())

s1.edge = 7
s1.area1()

#%% Method vs Functions

class Emp(object):
  
    age = 25
    salary = 1000 # $
  
    #method
    def ageSalartRatio(self):
      a = self.age / self.salary
      print("method: ",a)
      
e1 = Emp()
e1.ageSalartRatio()

#%%
    
#function
def ageSalaryRatio(age,salary):
    a = age/ salary
    print("function :",a)
    
ageSalaryRatio(30,3000)

#
def findArea(a,b):  #a = pi , b = r
    area = a*b**2
    print(area)
    return area
  
pi = 3.14
r = 5
area = 3.14*r**2
  
result1 = findArea(pi,r)

result2 =findArea(pi,10)
  
sum = result1 + result2

#%%

class Animal(object):
  
    def __init_(self,name,age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
      
    def getName(self):
        print(self.name)
      
      
a1 = Animal("dog",2)
a2 = Animal("cat",4)
a3 = Animal("bird",6)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

