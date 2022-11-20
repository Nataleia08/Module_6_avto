import re


def sanitize_file(source, output):
    with open(source, 'r') as fh1:
        with open(output, "w") as fh2:
            lines = fh1.readlines()
            n_line = []
            for i in lines:
                l = re.sub(r'\d', '', i)
                n_line.append(l)
            text = "".join(n_line)
            fh2.write(text)
            fh2.close()
        fh1.close()


sanitize_file("E:\\python-project-master\\\\4.txt",
              "E:\\python-project-master\\\\5.txt")
