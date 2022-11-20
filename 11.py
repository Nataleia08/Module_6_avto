def get_credentials_users(path):
    lines = []
    with open(path, 'rb') as fh:
        while True:
            fh.seek(0)
            line_b = fh.readline()
            if not len(line_b):
                break
            line = line_b.decode()
            n_line = line.removesuffix('\n')
            lines.append(n_line)
    return lines


get_credentials_users("E:\python-project-master\\2.txt")
