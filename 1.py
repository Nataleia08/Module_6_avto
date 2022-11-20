def total_salary(path):
    fh = open(path, 'r')
    mas_line = []
    sum = 0
    while True:
        line = fh.readline()
        mas_line.append(line)
        if not line:
            break
    fh.close()
    o = len(mas_line)-1
    mas_line.pop(o)
    for i in mas_line:
        k = i.split(",")
        l = k[1][0:4]
        sum = sum + float(l)

    return sum


total_salary("E:\python-project-master\\1.txt")
