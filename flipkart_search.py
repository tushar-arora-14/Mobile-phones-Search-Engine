import urllib.request as ur
from bs4 import BeautifulSoup as bs
query = input('Enter a product to search: ')
site1 = 'https://www.flipkart.com/search?q='+query+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
html1 = ur.urlopen(site1).read()
soup1 = bs(html1,'html.parser')
lst1 = soup1.findAll('div',{'class':'_1-2Iqu row'})
if len(lst1)==0:
  lst1 = soup1.findAll('div',{'class':'_3liAhj _1R0K0g'})
  i=0
  for container in lst1:
    i= i+1
    print(i, container.find(class_='_1vC4OE').get_text(), container.find(class_='_2cLu-l').get_text())
else:
  i = 0
  for container in lst1:
    i= i+1
    print(i, container.find(class_='_3wU53n').get_text(), container.find(class_='_1vC4OE _2rQ-NK').get_text())
