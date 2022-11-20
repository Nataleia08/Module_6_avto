def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for e_list in employee_list:
        for employee in e_list:
            fh.write(employee)
            fh.write('\n')
    fh.close()


write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], [
                        'Drake Mikelsson,19']], "E:\python-project-master\\2.txt")
