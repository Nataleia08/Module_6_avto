import base64


def encode_data_to_base64(data):
    data_cod = []
    for i in data:
        i_b = i.encode("utf-8")
        i_cod = base64.b64encode(i_b)
        i_c = i_cod.decode("utf-8")
        data_cod.append(i_c)
    return data_cod
