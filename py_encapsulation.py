# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:02:49 2019

@author: asus
"""

class BankAccount(object):
    
    def __init__(self,name,money,address):
        self.name = name # global
        self.__money = money #private
        self.address = address

    def getMoney(self):
        return self.__money
        
    def setMoney(self ,amount):
        self.__money = amount
        
    def __increase(self):
        self.__money = self.__money + 500
        
p1 = BankAccount("messi",1000,"barca")
p2 = BankAccount("neymar",2000,"paris")


print("get mothod : ", p1.getMoney())
p1.setMoney(5000)
print("after set mothod : ", p1.getMoney())

#p1.__increase()
#print("after raise : ", p1.getMoney())


