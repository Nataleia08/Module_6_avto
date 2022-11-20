def is_equal_string(utf8_string, utf16_string):
    utf8_string_orig = utf8_string.decode('utf-8')
    utf16_string_orig = utf16_string.decode('utf-16')
    if utf8_string_orig == utf16_string_orig:
        return True
    else:
        return False
