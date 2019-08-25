
from urllib.request import urlopen as uReq
import csv
from bs4 import BeautifulSoup as soup
import pandas as pd

page_url = "https://www.trendyol.com/koton---kadin--erkek-tekstil/butikdetay/323498"

uClient = uReq(page_url)

page_soup = soup(uClient.read(),"html.parser")
uClient.close()

containers = page_soup.findAll("div",{"class":"product"})

out_filename = "koton_products.csv"

headers = "Product-Name,Product-Sale-Rate,Product-Price "

#open file and wrtie headers
f = open(out_filename,"w")
f.write(headers)

names = []
sales = []
price = []

i = 0
for container in containers:
    names.append(container.findAll("div",{"class":"name"})[0].text)

    sales.append(container.findAll("div",{"class":"promotion-text"})[0].text)

    price.append(container.findAll("div",{"class":"discounted-price"})[0].text)

    names[i] = names[i][6:-12]
    print("Product Name: ",names[i])
    print("Product Sale Rate:",sales[i])
    print("Product Price:",price[i])
    print("-"*40)

    f.write(names[i] + "," + "," + sales[i] + "," + price[i] + "\n")

f.close()




