'''
listkey: 列表格式,作为转换字典的key
tuplelist: 长度为1的元组列表，元组中的值作为对应key的value
'''
def tuplelistToDic(listkey, tuplelist):
    resultDic={}
    for tuplex in tuplelist:
        if type(tuplex) == tuple and len(tuplex) == len(listkey):
            for index in range(len(tuplex)):
                resultDic[listkey[index]] = tuplex[index]
            return  resultDic
        else:
            print('tuplelist不是长度为1的元组列表,tuplelist='+tuplelist+';或者元组列表的长度和listkey的长度不等')

