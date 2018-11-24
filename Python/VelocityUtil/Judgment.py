def isDicContainKey(key, dic):
    '判断key值是否包含在字典中'
    flag = False
    if (key in dic.keys()):
        flag = True
    return flag