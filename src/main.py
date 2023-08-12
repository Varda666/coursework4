from employee_req import employee_request

if __name__ == '__main__':

    print("Добрый день")

    empl_request = employee_request.EmployeeRequest(employee_request.get_employee_request())
    employee_request.EmployeeRequest.get_vacancies_info(empl_request)
    list_vacs = employee_request.EmployeeRequest.get_vacancies_info_by_name(empl_request)
    employee_request.print_vacs_for_employee(list_vacs)
    list_vacs2 = employee_request.EmployeeRequest.get_vacancies_info_by_salary(empl_request)
    employee_request.print_vacs_for_employee(list_vacs2)
    print("Введите сколько вакансий с самой высокой з/п вы хотели бы посмотреть?")
    top_n = int(input())
    list_vacs3 = employee_request.EmployeeRequest.get_top_n_vacancies_info_by_salary(empl_request, top_n)
    employee_request.print_vacs_for_employee(list_vacs3)
    list_vacs4 = employee_request.EmployeeRequest.get_sorted_vacancies_info_by_date_of_publication(empl_request)
    employee_request.print_vacs_for_employee(list_vacs4)
    list_vacs5 = employee_request.EmployeeRequest.get_vacancies_info_by_area(empl_request)
    employee_request.print_vacs_for_employee(list_vacs5)
    print("Введите слово для поиска вакансий?")
    keyword = input()
    list_vacs6 = employee_request.EmployeeRequest.get_vacancies_info_by_keyword(empl_request, keyword)
    employee_request.print_vacs_for_employee(list_vacs6)


