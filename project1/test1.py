import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib

url = 'https://anime.eiga.com/program/'
url1= "https://anime1.me/category/2018%E5%B9%B4%E7%A7%8B%E5%AD%A3/%E9%9D%92%E6%98%A5%E8%B1%AC%E9%A0%AD%E5%B0%91%E5%B9%B4%E4%B8%8D%E6%9C%83%E5%A4%A2%E5%88%B0%E5%85%94%E5%A5%B3%E9%83%8E%E5%AD%B8%E5%A7%8A"

resp = requests.get(url)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "lxml")
#print(soup)
rows = soup.find_all('div', class_='animeSeasonBox')
#print(rows)
data = soup.find_all('p', class_='seasonAnimeTtl')
#print(data)

resp1 = requests.get(url1)
resp1.encoding = "utf-8"
soup1 = BeautifulSoup(resp1.text, "lxml")
#print(soup)
rows1 = soup1.find_all('div', class_='entry-content')
#print(rows1)
data1 = soup1.find_all("tr")
data2 = soup1.find_all("li")
data3 = soup1.find_all('input' ,class_="acpwd-pass" )
print(data3)
list = []
ttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
contents = [["NEW",ttime]]
contents1 = []
i = 0
for row3 in data2:
    
    t = row3.find_next()
    i = i + 1
    if i < 6: continue
    url_on = str(row3.find("a")["href"])
    contents.append([t.string,url_on])
    
    n = str(t.string).find(" [")
    word = str(t.string)[0:n]
    #print(word)
    list.append(word)
contents.append(["ALL"," "])
for row in data:
    title = row.find_next()
    url_o = "https://anime.eiga.com/" + row.find("a")["href"]
    #print(title.string)
    #print(url_o)
for row1 in data1:
    data2 = row1.find_all("td")
    c1 = row1.find_next("td")
    
    for row2 in data2:
        #c = row2.find_next("td")
        if str(row2) == "<td></td>": continue
        if str(row2.string) == "Anime1.me": continue
        #if str(c) == "None": continue
        #print(c)
        #contents.append(row2.string + "\t")
        if "</a>" not in str(row2): 
          if str(row2.string) in list : continue
          contents.append([row2.string,"None"])
          continue
        c1 = str(row2.find("a")["href"])
        #print(row2.string)
        c1 = "https://anime1.me/" + str(c1)
        if str(row2.string) in list : continue
        contents.append([row2.string, c1])
        #contents.append("\n")
#print(contents)
colname = ["ANIME","URL"]
df = pd.DataFrame(contents, columns = colname)
df.head()

