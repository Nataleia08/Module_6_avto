def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for k in users_info.keys():
            line = k + ":" + users_info[k] + "\n"
            b_line = line.encode()
            fh.write(b_line)
        fh.close()


save_credentials_users("E:\python-project-master\\2.txt",
                       {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})
