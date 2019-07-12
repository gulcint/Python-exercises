# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:30:53 2019

@author: asus
"""

def teksayi(sayi):
    return (sayi%2==1)
 

liste = range(1,20)

a = list(filter(teksayi,liste))

print(a)