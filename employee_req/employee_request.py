from vacancies_dir import vacancies


def get_employee_request():
    """Получает данные для запроса от пользователя"""
    emp_name = ''
    emp_area = ''
    emp_salary = ''
    print('Выберите сайт поиска иформации о вакансии - HH или SJ')
    emp_website = input()
    if emp_website in ['HH', 'SJ']:
        print('Введите название вакансии')
        emp_name = input(str())
        print('Введите город')
        emp_area = input(str())
        print('Введите уровень зарплаты вакансии')
        emp_salary = input()
    else:
        print('Сайт поиска информации указан неверно')
    return emp_website, emp_name, emp_area, emp_salary


def print_vacs_for_employee(list_vacs):
    try:
        for vac in list_vacs:
            print(f"""Вакансия {vac["name"]} в регионе {vac["area"]} с заработной платой от {vac["salary_from"]} руб., 
ссылка: {vac["url"]}
опубликована: {vac["date_of_publication"][:10]}"""
              )
    except TypeError:
        pass



class EmployeeRequest:

    def __init__(self, get_employee_request):
        self.emp_website = get_employee_request[0]
        self.emp_name = get_employee_request[1]
        self.emp_area = get_employee_request[2]
        self.emp_salary = get_employee_request[3]



    def get_vacancies_info(self):
        """Выводит список всех вакансий с сайта СД или ХХ"""
        vacancies_list = []
        if self.emp_website == 'HH':
            hh_api = vacancies.HeadHunterAPI()
            data = vacancies.HeadHunterAPI.get_vacancies(hh_api)
            vacs_json_file = vacancies.VacanciesToJsonFile()
            vacancies.VacanciesToJsonFile.add_vacancy_to_file(vacs_json_file, data)
            vacs = vacancies.VacanciesToJsonFile.get_vacancies_from_file(vacs_json_file)
            for vac in vacs:
                vacancies_list.append(vac)

        elif self.emp_website == 'SJ':
            sj_api = vacancies.SuperJobAPI()
            data = vacancies.SuperJobAPI.get_vacancies(sj_api)
            vacs_json_file = vacancies.VacanciesToJsonFile()
            vacancies.VacanciesToJsonFile.add_vacancy_to_file(vacs_json_file, data)
            vacs = vacancies.VacanciesToJsonFile.get_vacancies_from_file(vacs_json_file)
            for vac in vacs:
                vacancies_list.append(vac)

        return vacancies_list

    def get_vacancies_info_by_name(self):
        """Выводит список вакансий по низванию вакансии"""
        suitable_vacancies_list = []
        vacs = self.get_vacancies_info()
        for vac in vacs:
            if self.emp_name in vac["name"]:
                if int(self.emp_salary) <= int(vac["salary_from"]):
                    suitable_vacancies_list.append(vac)
            else:
                    pass
        if len(suitable_vacancies_list) == 0:
            print('Нет вакансий с такой зарплатой')
        else:
            return suitable_vacancies_list

    def get_vacancies_info_by_salary(self):
        """Выводит список вакансии с определенным уровнем зп """
        suitable_vacancies_list = []
        vacs = self.get_vacancies_info()
        for vac in vacs:
            if int(self.emp_salary) <= int(vac["salary_from"]):
                suitable_vacancies_list.append(vac)
            else:
                pass
        if len(suitable_vacancies_list) == 0:
            print('Нет вакансий с такой зарплатой')
        else:
            return suitable_vacancies_list

    def get_top_n_vacancies_info_by_salary(self, top_n: int):
        """Выводит список вакансии с само большой зп"""
        try:
            list_top_n_vacancies_info_by_salary = sorted(self.get_vacancies_info(), key=lambda d: d["salary_from"])
            return list_top_n_vacancies_info_by_salary[:top_n]
        except FileNotFoundError:
            print('Введено не целое число')

    def get_sorted_vacancies_info_by_date_of_publication(self):
        """Сортирует вакансии по дате публикаци и выводит список"""
        list_vacancies_info_by_date_of_publication = sorted(self.get_vacancies_info(), key=lambda d: d["date_of_publication"])
        return list_vacancies_info_by_date_of_publication

    def get_vacancies_info_by_area(self):
        """Выводит список вакансий в определенном городе"""
        list_vacancies_info_by_area = []
        vacs = self.get_vacancies_info()
        for vac in vacs:
            if self.emp_area in vac["area"]:
                list_vacancies_info_by_area.append(vac)
            else:
                pass
        if len(list_vacancies_info_by_area) == 0:
            print('Нет вакансий в данном регионе')
        else:
            return list_vacancies_info_by_area

    def get_vacancies_info_by_keyword(self, keyword):
        """Выводит список вакансий по ключевому слову"""
        list_vacancies_info_by_keyword = []
        vacs = self.get_vacancies_info()
        for vac in vacs:
            if keyword in vac.values():
                list_vacancies_info_by_keyword.append(vac)
            else:
                pass
        if len(list_vacancies_info_by_keyword) == 0:
            print('Вакансии по ключевому слову не найдены')
        else:
            return list_vacancies_info_by_keyword






