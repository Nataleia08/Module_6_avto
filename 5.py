def get_cats_info(path):
    with open(path, 'r') as fh:
        list_cats = []
        while True:
            line = fh.readline()
            if not len(line):
                break
            cat = {}
            list_cat = line.split(',')
            cat["id"] = list_cat[0]
            cat["name"] = list_cat[1]
            cat["age"] = list_cat[2].removesuffix('\n')
            list_cats.append(cat)
        fh.close()
    return list_cats
