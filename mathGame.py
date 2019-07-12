# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:16:09 2019

@author: asus
"""

""" 
Math Game 

* Random olarak matematik işlemi belirlenir. (toplama , çıkarma,bölme
                                                çarpma, faktöriyel)
* Daha sonra rasgele sayilar belirlenir ve belirlenen işlem uygulanır.
* Kullanıcıdan cevap istenir.
* Eğer cevap doğru ise kullanıcı 10 puan kazanır.
* Yanlış ise 5 puan kaybeder.
* Kullanıcı 10 puanla başlar.
* Kullanıcının puanı 0 olunca oyunu kaybeder ve oyun sonlanır.
* Kullanıcının puanı 50 olunca oyunu kazanır ve oyun sonlanır.

"""

# toplama 0 
# cikarma 1  
# bolme 2 
# carpma 3
# faktoriyel 4

import time
import random
import math


islemler = range(0,5)
opr =["Toplama","Çıkarma","Bölme","Çarpma","Faktöriyel"]
puan = 10


while(puan>0 & puan <50):
        
    print("-"*30)
    print("Matematik oyunu başlıyor.")
    print("Başlangıç puanınız : ",puan)
    print("-"*30)
    time.sleep(1)
    
    print("-"*30)
    print("Matematik işlemi belirleniyor.")
    print("-"*30)
    time.sleep(1)
    
    islem = random.choice(islemler)
    
    
    if(islem==4): # factoriyel için 1 tane rasgele sayi üretilir.
        print("İşleminiz :",opr[islem])
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi = random.randint(1,100)
        print("Sayi :" ,sayi)
        
        sonuc = math.factorial(sayi)
        time.sleep(1)
        cevap = int(input("Cevabınızı girin : "))
        
    elif (islem==0):
        print("İşleminiz :",opr[islem])
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi1 = random.randint(1,100)
        print("Sayi1 :" ,sayi1)
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi2 = random.randint(1,100)
        print("Sayi2 :" ,sayi2)
        
        sonuc = sayi1 + sayi2
        time.sleep(1)
        cevap = int(input("Cevabınızı girin : "))
        
    elif (islem==1):
        print("İşleminiz :",opr[islem])
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi1 = random.randint(1,100)
        print("Sayi1 :" ,sayi1)
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi2 = random.randint(1,100)
        print("Sayi2 :" ,sayi2)
        
        sonuc = sayi1 - sayi2
        time.sleep(1)
        cevap = int(input("Cevabınızı girin : "))
        
    elif (islem==2):
        print("İşleminiz :",opr[islem])
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi1 = random.randint(1,100)
        print("Sayi1 :" ,sayi1)
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi2 = random.randint(1,100)
        print("Sayi2 :" ,sayi2)
        
        sonuc = sayi1 / sayi2
        time.sleep(1)
        cevap = int(input("Cevabınızı girin : "))
    
    elif (islem==3):
        print("İşleminiz :",opr[islem])
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi1 = random.randint(1,100)
        print("Sayi1 :" ,sayi1)
        print("Rasgele sayi belirleniyor.")
        time.sleep(1)
        sayi2 = random.randint(1,100)
        print("Sayi2 :" ,sayi2)
        
        sonuc = sayi1 * sayi2
        time.sleep(1)
        cevap = int(input("Cevabınızı girin : "))
        
    if(sonuc == cevap):
        puan += 10
    else :
        puan -= 5
    
    if(puan == 0):
        print("Oyunu kaybettiniz! ")
    elif (puan  == 50) :
        print("Oyunu kazandınız . :)") 
        
