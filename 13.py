import shutil


def create_backup(path, file_name, employee_residence):
    p = path + "/" + file_name
    with open(p, 'wb') as fh:
        for k in employee_residence.keys():
            line = k + " " + employee_residence[k] + "\n"
            b_line = line.encode()
            fh.write(b_line)
    shutil.make_archive('backup_folder', 'zip', path)
    p_zip = path + "/" + "backup_folder.zip"
    return p_zip
