import requests
import chardet
from bs4 import BeautifulSoup

# url = ("https://www.youtube.com/playlist?list=PLA0M1Bcd0w8yU5h2vwZ4LO7h1xt8COUXl") headers = { "User-Agent":
# "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36" } req =
# requests.get(url, headers=headers) src = req.text

# encoding = chardet.detect(src.encode())['encoding']
# with open("index.html", "w") as file:
#    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
link = soup.find_all(class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")
# for i in link:
#    print(i.text)
with open("django_learning_topics.txt", "w") as file:
    for i in link:
        file.write(i.text)
