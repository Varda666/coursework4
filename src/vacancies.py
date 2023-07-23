
from abc import ABC, abstractmethod
import requests
import json
import pandas as pd
import csv

class AbstractAPI(ABC):
    pass

class HeadHunterAPI(AbstractAPI):
    pass

class SuperJobAPI(AbstractAPI):
    pass

class Vacancies():


    def __init__(self):
        """Где мы задаем тип данных тут?"""
        self.response = requests.get('https://api.hh.ru/vacancies')
        self.id = self.d["items"]["id"]
        self.name = self.response["items"]["name"]
        self.date_of_publication = self.response["items"]["published_at"]
        self.salary_from = self.response["items"]["salary"]["from"]
        self.currency = self.response["items"]["salary"]["from"]
        self.url = f'https://hh.ru/vacancy/{self.id}'

        """Что значит валидировать данные, которыми инициализируются его атрибуты?
        Как понять какие атрибуты должныбыть приватными?"""

    def compare_salaries(self):
        """ Как конкретно нужно сравнивать зарплаты? Магические методы надо испрльзовать __lt__, __gt__ и тд?
        Разниуа между == и =?
        Тестирование нужно?

        """
        max_salary = 0
        best_vacancy = ''
        if self.currency == "RUR":
            if self.salary_from > max_salary:
                max_salary == self.salary_from
                best_vacancy = self.name
        if self.currency == "USD":
            rur_currency = self.currency * 90
            if rur_currency > max_salary:
                max_salary == rur_currency
                best_vacancy = self.name
        return f' {best_vacancy} с з\п {max_salary}'


class AbstractVacanciesToFile(ABC):

    @abstractmethod
    def add_vacancy_to_file(self):
        pass

class VacanciesToJsonFile(Vacancies, AbstractVacanciesToFile):

    def __init__(self):
        """Нужно ли добавлять тут информацию снова или как-то унаследовать от класса родилтеля?"""
        super().__init__()

    def add_vacancy_to_json_file(self):
        with open("vacancies.json", "w", encoding='utf-8') as file:
            json.dump(self.response.json(), file, ensure_ascii=False)

class VacanciesToCsvFile(Vacancies, AbstractVacanciesToFile):

    def __init__(self):
        """Нужно ли добавлять тут информацию снова или как-то унаследовать от класса родилтеля?"""
        super().__init__()

    def add_vacancy_to_csv_file(self):
        with open('vacancies.csv', mode="w", encoding='utf-8') as file:
            names = ["id", "name", "date_of_publication", "salary_from", "currency", "url"]
            file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            for i in self.response["items"]:
                file_writer.writerow(i)



class VacanciesToTxtFile(Vacancies, AbstractVacanciesToFile):

    def __init__(self):
        """Нужно ли добавлять тут информацию снова или как-то унаследовать от класса родилтеля?"""
        super().__init__()

    def add_vacancy_to_txt_file(self):
        with open("vacancies.txt", "w", encoding='utf-8') as file:
            json.loads(self.response.text)








