import json

num_less = input(f"Введите нужный вам урок:  ")
with open('data.json') as f:
    data = json.load(f)

for key, value in data.items():
    if key == "id_video "+ num_less:
        if value['title'][2].isdigit():
            print(f"Видео номер {value['title'][1:3]}")
            print(f"Название : {value['title']}")
            print(f"Ссылка на видео {value['url']}", end="\n")
        else:
            print(f"Видео номер {value['title'][1]}")
            print(f"Название : {value['title']}")
            print(f"Ссылка на видео {value['url']}", end="\n")
        