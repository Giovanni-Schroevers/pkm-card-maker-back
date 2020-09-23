import re

camel_pat = re.compile(r'([A-Z])')


def convert(s):
    a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
    return a.sub(r'_\1', s).lower()


def convert_array(a):
    newArr = []
    for i in a:
        if isinstance(i, list):
            newArr.append(convert_array(i))
        elif isinstance(i, dict):
            newArr.append(convert_JSON(i))
        else:
            newArr.append(i)
    return newArr


def convert_JSON(j):
    out = {}
    for k in j:
        newK = convert(k)
        if isinstance(j[k], dict):
            out[newK] = convert_JSON(j[k])
        elif isinstance(j[k], list):
            out[newK] = convert_array(j[k])
        else:
            out[newK] = j[k]
    return out

