def getVariableValueList(testcontex,list):
    '通过同名字符串获取同名变量的值'
    for index in range(len(list)):
        value = list[index]
        if type(value) == str and value.startswith('$'):
            value = value.replace('$', '')
            list[index] = testcontex.get(value)
    # print(list)
    return list


def getVariableValueDic(testcontex,dic):
    '通过同名字符串获取同名变量的值'
    for key in list(dic):
        tempvalue = dic.get(key)
        if type(tempvalue) == str and tempvalue.startswith('$'):
            value = tempvalue.replace('$', '')
            dic[key] =testcontex.get(value)
    return dic

def getvaluefromDic(dic,tb,tablename):
    for key in dic:
        actualvalue = dic[key]
        tb.add_row([tablename, key, "C", actualvalue, actualvalue, True])