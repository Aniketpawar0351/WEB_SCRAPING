#import rquired module
import requests
#import BeautifulSoup class from bs4
from bs4 import BeautifulSoup

url=input("enter url: ")

#get the html in string
r=requests.get(url)
htmlContent=r.content

#paras the html
soup=BeautifulSoup(htmlContent,'html.parser')

#travers html tree
title=soup.title

soup=BeautifulSoup(htmlContent,'html.parser')

#print(soup)
#print(title)

#print(soup.get_text())
#print(soup.find('p').get_text())
paras=soup.find_all('p')
print(paras)
#print(soup.find('p'))
