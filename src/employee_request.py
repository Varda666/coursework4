import vacancies


class EmployeeRequest:

    def __init__(self):
        print('Выберите сайт поиска иформации о вакансии - HH или SJ')
        self.emp_website = input()
        if self.emp_website in ['HH', 'SJ']:
            print('Введите название вакансии')
            self.emp_name = input(str())
            print('Введите уровень зарплаты вакансии')
            self.emp_salary = input()
            print('Введите период публикации зарплаты вакансии')
            self.emp_date_of_publication = input()
        else:
            print('Сайт поиска информации указан неверно')




    def get_vacancies_info_by_name(self):
        '''Где разделить HH и SJ?'''
        suitable_vacancies_list = []
        if self.emp_website == 'HH':
            vacs = vacancies.Vacancies()
            if self.emp_name in vacs.name:
                if self.emp_salary >= vacs.salary_from:
                    suitable_vacancies_list.append(vacs.url)
                else:
                    pass
            else:
                print('Нет вакансий с таким именем')

        elif self.emp_website == 'SJ':
            vacs = vacancies.Vacancies()
            if self.emp_name in vacs.name:
                if self.emp_salary >= vacs.salary_from:
                    suitable_vacancies_list.append(vacs.url)
                else:
                    pass
            else:
                print('Нет вакансий с таким именем')

        return suitable_vacancies_list

    def get_vacancies_info_by_salary(self):
        '''Где разделить HH и SJ?'''
        suitable_vacancies_list = []
        if self.emp_website == 'HH':
            vacs = vacancies.Vacancies()
            if self.emp_salary >= vacs.salary_from:
                suitable_vacancies_list.append(vacs.url)
            else:
                pass
        if len(suitable_vacancies_list) == 0:
            print('Нет вакансий с такой зарплатой')
        else:
            return suitable_vacancies_list









