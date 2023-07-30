import employee_request, vacancies


if __name__ == '__main__':

    print("Добрый день")
    empl_request = employee_request.EmployeeRequest(employee_request.get_employee_request())
    employee_request.EmployeeRequest.get_vacancies_info(empl_request)
    employee_request.EmployeeRequest.get_vacancies_info_by_name(empl_request)
    # employee_request.EmployeeRequest.get_vacancies_info_by_salary(empl_request)
    print("Введите сколько вакансий с самой высокой з/п вы хотели бы посмотреть?")
    top_n = input()
    # employee_request.EmployeeRequest.get_top_n_vacancies_info_by_salary(empl_request, top_n)
    employee_request.EmployeeRequest.get_sorted_vacancies_info_by_date_of_publication(empl_request)
    employee_request.EmployeeRequest.get_vacancies_info_by_area(empl_request)
    print("Введите слово для поиска вакансий?")
    keyword = input()
    employee_request.EmployeeRequest.get_vacancies_info_by_keyword(empl_request, keyword)


