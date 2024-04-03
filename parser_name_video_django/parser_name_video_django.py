import requests
import chardet
from bs4 import BeautifulSoup
import json


# url = ("https://www.youtube.com/playlist?list=PLA0M1Bcd0w8yU5h2vwZ4LO7h1xt8COUXl") headers = { "User-Agent":
# "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36" } req =
# requests.get(url, headers=headers) src = req.text

# encoding = chardet.detect(src.encode())['encoding']
# with open("index.html", "w") as file:
#    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
total = soup.find_all(class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")



#with open("django_learning_topics.txt", "w", encoding="utf-8") as file:
#    for i in total[8:11]:
#        file.write(i.text)



data = {}
c = 1
for i in total[8:11]:
    data.update({f"id_video {c}":{
        "title": i.text.replace("\n          ", ""),
        "url": i.get("href")
    } 
                 })
    c+=1
    
    
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    