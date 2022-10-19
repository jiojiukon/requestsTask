import requests
from pprint import pprint


class YaUploadr:
    def __init__(self,token:str):
        self.token = token

    def get_headers(self):
         return {'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}


    def upload(self,file_path:str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        get_link = requests.get(url=url, headers=self.get_headers(), params={"path": file_path, 'overwrite' : 'true'}).json()
        file = open(file_path, 'rb')
        upload_link = get_link['href']
        upload = requests.put(upload_link, data = file )

        return print(f'Код ответа: {upload.status_code}')

if __name__ == '__main__':
#Загрузка файла на яндекс диск
    token = ''
    yandex = YaUploadr(token)
    path_to_file ='' 
    yandex.upload(path_to_file)

#Определение самого умного:
    heros_int = {}

    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    all_info = response.json()

    for i in all_info:
        name = i['name']
        intelligence = i['powerstats']['intelligence']
        if name == 'Hulk' or name == 'Captain America' or name == 'Thanos':
            heros_int[name] = int(intelligence)

    for name, intell in heros_int.items():
        if intell == max(heros_int.values()):
            print(f'{name} - самый умный из выбранных героев')