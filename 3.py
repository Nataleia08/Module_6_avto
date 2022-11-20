def read_employees_from_file(path):
    fh = open(path, 'r')
    fh.seek(0)
    employees_list = []
    while True:
        line = fh.readline()
        if not len(line):
            break
        employee_1 = line.removesuffix('\n')
        employees_list.append(employee_1)
    fh.close()
    return employees_list


read_employees_from_file("E:\\python-project-master\\\\1.txt")
