def dicAnd(dict):
    '字典拼装字符串'
    condiction = []
    for i in dict.keys():
        condiction.append((i + "=" + "'" + dict[i] + "'"))
    return " and ".join(condiction)
