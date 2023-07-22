import json

import requests

# response = requests.get('https://api.hh.ru/vacancies')
# response.headers['User-Agent']

url = 'https://api.hh.ru/vacancies'
headers = {'user-agent': 'MyApp/1.0'}
r = requests.get(url)



# #
with open("test.json", "w", encoding='utf-8') as file:
    json.dump(r.json(), file, ensure_ascii=False)
#
# with open('test.json') as json_file:
#     data = json.load(json_file)
# print(len(response.json()['items']))