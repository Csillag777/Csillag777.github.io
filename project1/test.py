import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://movies.yahoo.com.tw/chart.html'

# GET request from url and parse via BeautifulSoup
resp = requests.get(url)
resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
soup = BeautifulSoup(resp.text, 'lxml')
# parse colname 
rows = soup.find_all('div', class_='tr')
# get strings and convert into list
colname = list(rows.pop(0).stripped_strings) 

contents = []
for row in rows:
    thisweek_rank = row.find_next("div", attrs={"class":"td"})
    updown = thisweek_rank.find_next("div")
    lastweek_rank = updown.find_next("div")
    
    if thisweek_rank.string == str(1):
        movie_title = lastweek_rank.find_next("h2")
    else:
        movie_title = lastweek_rank.find_next("div", attrs = {"class" : "rank_txt"})
       
    #print(movie_title)
    #exit()
    release_date = movie_title.find_next("div", attrs = {"class": "td"})
    trailer = lastweek_rank.find_next("div", attrs = {"class": "td"})
    trailer_address = trailer.find("a")["href"]
    stars = row.find("h6", attrs = {"class": "count"})
    
    lastweek_rank = lastweek_rank.string if lastweek_rank.string else ""
    
    c=  [thisweek_rank.string, lastweek_rank, movie_title.string, release_date.string, trailer_address, stars.string]
    
    print(c)
    
    contents.append(c)
    
df = pd.DataFrame(contents, columns = colname)
df.head()

import os
import datetime

cwd = os.getcwd()
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%Y%m%d")

#print(cwd)
filename = os.path.join(cwd , "yahoo_movie_rank.csv".format(timestamp))
df.to_csv(filename, index = False)
print("save csv to " + format(filename))
