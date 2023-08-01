import json

import requests
import csv
import pandas as pd

# response = requests.get('https://api.hh.ru/vacancies')
# response.headers['User-Agent']
#
# url = 'https://api.hh.ru/vacancies'
# headers = {'User-Agent': 'MyApp/23.0'}
# r = requests.get(url, headers=headers)


class Vacancies():
    def __init__(self, id, name, area, date_of_publication, url):
        self.id = id
        self.name = name
        self.area = area
        self.date_of_publication = date_of_publication
        # self.salary_from = salary_from
        self.url = url

    def __repr__(self):
        return f'{self.id}, {self.name}'

url = 'https://api.hh.ru/vacancies'
payload = {"per_page": 100}
responce = requests.get(url, params=payload)
data = responce.json()["items"]
vacancies = [Vacancies(id=item["id"],
                       name=item["name"],
                       area=item["area"]["name"],
                       date_of_publication=item["published_at"],
                       # salary_from=item["salary"]["from"],
                       url=f'https://hh.ru/vacancy/{id}')
             for item in data]

print(type(vacancies))


#         file_writer.writerow(i)
#     with open('vacancies.csv', mode="r", encoding='utf-8') as file:
#         file_reader = csv.reader(file, delimiter=",")
#         return file_reader
# # #

# url = 'https://api.hh.ru/vacancies'
# payload = {"per_page": 100}
# responce = requests.get(url, params=payload)
# #
# with open("test.json", "w", encoding='utf-8') as file:
#     json.dump(r.json(), file, ensure_ascii=False, indent=2)
#
# with open('test.json') as json_file:
#     data = json.load(json_file)
# print(len(response.json()['items']))

# url = 'https://api.hh.ru/vacancies'
# payload = {"per_page" : 100}
# responce = requests.get(url, params=payload)
# data = responce.json()["items"]
# vacancies = []
# vacancy = {}
# for item in data:
#     for vacancy in vacancies:
#
#         vacancy["id"]=item["id"]
#         name=item["name"]
#         date_of_publication=item["published_at"]
#         # salary_from=item["salary"]["from"]
#         url=f'https://hh.ru/vacancy/{id}'
#     vacancies.append(vacancy)
# # with open("vacancies.json", "w", encoding='utf-8') as file:
# #     json.dump(vacancies, file, ensure_ascii=False)
#
# with open('vacancies.csv', mode="w", encoding='utf-8') as file:
#     names = ["id", "name", "date_of_publication", "salary_from", "currency", "url", "requirements"]
#     file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     """Как внести в csv только нужные нам поля?"""
#     for i in vacancies:
#         file_writer.writerow(i)

# url = "	https://api.superjob.ru/2.0/vacancies/"
# headers = {"X-Api-App-Id": "v3.r.118887071.4fb17eb73379f8a33cbae75aa072f91e2a86f68c.2bde35d83100bea436d45c2646f1b168fe578e8e"}
#
#
# response = requests.get(url, headers=headers)
# data = response.json()["objects"]
# # print(type(data))
# #
# #
# #
# # vacancy = {}
# # for item in data:
# #     vacancy["id"] = item["id"]
# #     vacancy["name"] = item["profession"]
# #     vacancy["area"] = item["town"]["title"]
# #     vacancy["date_of_publication"] = item["date_published"]
# #     vacancy["salary_from"] = item["payment_from"]
# #     vacancy["url"] = f'https://api.superjob.ru/2.0/vacancies/{id}/'
# # with open("vacancies.json", "w", encoding='utf-8') as file:
# #     json.dump(data, file, ensure_ascii=False)
#
# newlist = sorted(data, key=lambda d: d["payment_from"])
#
# print(newlist)
# #
# #     list_top_N_vacancies_info_by_salary =
# #
# # print(list_top_N_vacancies_info_by_salary)

# print(vacancies)
# vac_salary_list = []
# for vacancy in vacancies:
#
#     vac_salary_list.append(vacancy["salary_from"])
#
# print(vac_salary_list)

#
# with open("vacancies.json", "w", encoding='utf-8') as file:
#      json.dump(vacancy, file, ensure_ascii=False)


