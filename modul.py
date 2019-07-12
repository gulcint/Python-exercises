# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:30:21 2019

@author: asus
"""

""" 
Matematik oyunu

program rasgele işlem soracak toplama çıkarma..
iki tane sayı verecek toplama çıkrma ..
fact ise  tek sayi verecek
bizde cevabımızız gireceğiz 
doğru mu yanlış mı ekrana basılacak.

"""
 
import random

islemler = ["toplama","carpma","bolme","factoriyel","cıkarma"]
sayilar  = [1,2,42,78,95,45,78,1,24,6,7,9,21]

islem = random.choice(islemler)
print(islem)

if islem == "factoriyel":
    sayi = random.choice(sayilar)
    print("Lütfen " + islem + "yapınız ")
    print("Sayi : " ,sayi)
if islem =="toplama":
    
    sayi1 = random.choice(sayilar)
    sayi2 = random.choice(sayilar)
    
    print("Lütfen " ,islem , "yapınız ")
    print("Sayi1 :" ,sayi1)
    print("Sayi2 :" , sayi2)
    
    sonuc = sayi1 + sayi2
if islem =="cikarma":
    
    sayi1 = random.choice(sayilar)
    sayi2 = random.choice(sayilar)
    
    print("Lütfen " ,islem , "yapınız ")
    print("Sayi1 :" ,sayi1)
    print("Sayi2 :" , sayi2)
    
    sonuc = sayi1 - sayi2
if islem =="carpma":
    
    sayi1 = random.choice(sayilar)
    sayi2 = random.choice(sayilar)
    
    print("Lütfen " ,islem , "yapınız ")
    print("Sayi1 :" ,sayi1)
    print("Sayi2 :" , sayi2)
    
    sonuc = sayi1 * sayi2
if islem =="bolme":
    
    sayi1 = random.choice(sayilar)
    sayi2 = random.choice(sayilar)
    
    print("Lütfen " ,islem , "yapınız ")
    print("Sayi1 :" ,sayi1)
    print("Sayi2 :" , sayi2)
    
    sonuc = sayi1 / sayi2
    
    
cevap = int(input("Cevabi giriniz :"))

if sonuc == cevap :
    print("Tebrikler Bildiniz ")
else : 
    print("Bilemediniz")
    
durum = input("Oyuna devam etmek ister misiniz ? E \ H")
    
    
