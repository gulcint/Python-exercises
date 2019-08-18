from bs4 import  BeautifulSoup
import requests

url = 'https://hthayat.haberturk.com/gunluk-burc-yorumlari-18-agustos-2019-pazar-1071938'

r = requests.get(url,timeout=5)
content = r.content
haber = BeautifulSoup(content,"html.parser")

textContent = []

print("-"*25)
print("Günlük Burç Yorumları")
print("-"*25)

print("1 -  KOÇ\n"
      "2 -  BOĞA\n"
      "3 -  İKİZLER\n"
      "4 -  YENGEÇ\n"
      "5 -  ASLAN\n"
      "6 -  BAŞAK\n"
      "7 -  TERAZİ\n"
      "8 -  AKREP\n"
      "9 -  YAY\n"
      "10 - OĞLAK\n"
      "11 - KOVA\n"
      "12 - BALIK\n")

for i in range(25):
    paragraf = haber.find_all("p",{"class":"MsoNormal"})[i].text
    textContent.append(paragraf)

del textContent[0]

liste1 = ["KOÇ","BOĞA","iKİZLER","YENGEÇ","ASLAN","BAŞAK","TERAZİ","AKREP","YAY","OĞLAK","KOVA","BALIK"]
liste2 = []

for index, value  in enumerate(textContent):
    if (index % 2 == 1):
        liste2.append(value)

zipping = zip(liste1,liste2)
dic = dict(zipping)

print("-"*60)
print(" Günlük yorumunu öğrenmek istediğiniz burcun adını giriniz :")
print("-"*60)

burc = input("")

print(dic[burc])

