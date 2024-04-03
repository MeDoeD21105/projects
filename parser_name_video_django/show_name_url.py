import json


with open('data.json') as f:
    data = json.load(f)

for key, value in data.items():
    if value['title'][2].isdigit():
        print(f"Видео номер {value['title'][1:3]}")
        print(f"Название : {value['title']}")
        print(f"Ссылка на видео {value['url']}", end="\n")
    else:
        print(f"Видео номер {value['title'][1]}")
        print(f"Название : {value['title']}")
        print(f"Ссылка на видео {value['url']}", end="\n")
        