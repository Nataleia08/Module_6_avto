def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        result = {}
        while True:
            line = fh.readline()
            if not line:
                break
            if line.find(search_id) != -1:
                line_list = line.removesuffix('\n').split(',')
                result["id"] = line_list[0]
                result["name"] = line_list[1]
                result["ingredients"] = line_list[2:]
                fh.close()
                return result
        fh.close()
    return None
