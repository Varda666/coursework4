from abc import ABC, abstractmethod
import requests
import json
import csv
from datetime import datetime
import os


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class AbstractVacancies(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __call__(self):
        pass


class Vacancies(AbstractVacancies):
    def __init__(self, id, name, area, date_of_publication, salary_from, url):
        self.id = id
        self.name = name
        self.area = area
        self.date_of_publication = date_of_publication
        self.salary_from = salary_from
        self.url = url

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки"""
        return f'Вакансия {self.name} - Место {self.area} с зарплатой {self.salary_from}'

    def __add__(self, other):
        """Возвращает сумму з.п двух вакансий"""
        return self.salary_from + other.salary_from

    def __call__(self, *args, **kwargs):
        """Возвращает дату публикации вакансии"""
        return self.date_of_publication


class HeadHunterAPI(AbstractAPI):

    def get_vacancies(self):
        """Получает список всех вакансий как объектов класса Vacancies с сайта ХХ"""
        url = 'https://api.hh.ru/vacancies'
        payload = {"per_page": 100}
        responce = requests.get(url, params=payload)
        data = responce.json()["items"]
        list_vac_obj = []
        for item in data:
            id = item["id"]
            name = item["name"]
            area = item["area"]["name"]
            date_of_publication = item["published_at"]
            if item["salary"]["from"] == "null":
                salary_from = 0
            else:
                salary_from = item["salary"]["from"]
            vacancy = Vacancies(id=id,
                                  name=name,
                                  area=area,
                                  date_of_publication=date_of_publication,
                                  salary_from=salary_from,
                                  url=f'https://hh.ru/vacancy/{id}')
            list_vac_obj.append(vacancy)
            return list_vac_obj


class SuperJobAPI(AbstractAPI):

    def get_vacancies(self):
        """Получает список всех вакансий как объектов класса Vacancies с сайта СД"""
        sj_api_key = os.getenv('X-Api-App-Id')
        url = "	https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": sj_api_key}
        response = requests.get(url, headers=headers)
        data = response.json()["objects"]
        vacancies = [Vacancies(id=item["id"],
                               name=item["profession"],
                               area=item["town"]["title"],
                               date_of_publication=datetime.fromtimestamp(
                                   int(item["date_published"])).strftime('%d-%m-%Y %H.%M'),
                               salary_from=item["payment_from"],
                               url=f'https://api.superjob.ru/2.0/vacancies/{id}/')
                     for item in data]
        return vacancies


class AbstractVacanciesToFile(ABC):

    @abstractmethod
    def add_vacancy_to_file(self, data):
        pass

    @abstractmethod
    def get_vacancies_from_file(self):
        pass


class VacanciesToJsonFile(AbstractVacanciesToFile):

    def add_vacancy_to_file(self, list_obj):
        """Записывает список всех вакансий как объектов класса Vacancies с сайта СД или ХХ в json-файл"""
        with open("../json_files/vacancies.json", "w", encoding='utf-8') as file:
            json.dump([ob.__dict__ for ob in list_obj], file, ensure_ascii=False)

    def get_vacancies_from_file(self):
        """Получает список всех вакансий(словари) из json-файла"""
        with open("../json_files/vacancies.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            return data


class VacanciesToCsvFile(HeadHunterAPI, AbstractVacanciesToFile):

    def add_vacancy_to_file(self, data):
        """Записывает список всех вакансий как объектов класса Vacancies с сайта СД или ХХ в csv-файл"""
        with open('vacancies_dir.csv', mode="w", encoding='utf-8') as file:
            names = ["id", "name", "area", "date_of_publication", "salary_from", "url"]
            file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            hh_api = HeadHunterAPI()
            for i in HeadHunterAPI.get_vacancies(hh_api):
                file_writer.writerow(i)

    def get_vacancies_from_file(self):
        """Получает построчно все вакансии из csv-файла"""
        with open('vacancies_dir.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return file_reader


class VacanciesToTxtFile(HeadHunterAPI, AbstractVacanciesToFile):

    def add_vacancy_to_file(self, data):
        """Записывает список всех вакансий как объектов класса Vacancies с сайта СД или ХХ в txt-файл"""
        with open("vacancies_dir.txt", "w", encoding='utf-8') as file:
            hh_api = HeadHunterAPI()
            json.dump(HeadHunterAPI.get_vacancies(hh_api), file, ensure_ascii=False)

    def get_vacancies_from_file(self):

        """Получает список всех вакансий(словари) из txt-файла"""
        with open("vacancies_dir.txt", "r", encoding='utf-8') as file:
            return file.readline()
