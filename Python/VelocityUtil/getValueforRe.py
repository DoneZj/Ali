import re
import traceback
from Python.VelocityUtil.Logging import Logger


def getstrReState(strvalue,restr):
    '通过正则表达式(字符串)匹配字符串，返回匹配的结果是否有值的状态'
    '''
    :param strvalue: 需要匹配的字符串对象
    :param restr: 匹配的正则表达式规则
    :return: 匹配后是否有值的状态
    '''
    pattern = re.compile(str(restr))
    result = pattern.search(str(strvalue))
    flag = False
    if result != None:
        flag = True
    return  flag

def getdicReState(strvalue,restr,tablename,tb):
    '通过正则表达式(字典类型)匹配字典类型，返回匹配的结果是否有值的状态'
    '''
    :param strvalue: 需要匹配的字符串对象(字典类型)
    :param restr: 匹配的正则表达式规则(字典类型)
    :return: 匹配后是否有值的状态
    '''
    log = Logger().logger
    res = []
    for key in restr:
        reg = restr[key]        #得到正则表达式
        targetvalue = strvalue[key]         #得到正则需要匹配的对象
        pattern = re.compile(str(reg))
        result = pattern.search(str(targetvalue))
        try:
            assert result != None
            tb.add_row([tablename, key, "R", targetvalue, reg, True])
        except AssertionError as e:
            log.debug(traceback.format_exc()+'ReError:[Column=%s (Flag=R)]:actualValue(%s) != expectvalue(%s)'%(key,targetvalue,reg))
            res.append([key,targetvalue, reg])
            continue
    return  res

def getReValue(strvalue,restr):
    '通过正则表达式匹配，返回匹配的结果'
    '''
    :param strvalue: 需要匹配的字符串对象
    :param restr: 匹配的正则表达式规则
    :return: 匹配后的结果，list类型
    '''
    pattern = re.compile(str(restr))
    result = pattern.findall(str(strvalue))
    return result


if __name__ == '__main__':

    conditionR = {'LoginName': '.'}
    actualValue = {'UserInfoID': 4, 'LoginName': 'zgf', 'State': 1, 'HospitalID': 1, 'Sex': 1, 'UserType': 1, 'UserName': '查国芬',
     'Password': 'e10adc3949ba59abbe56e057f20f883e', 'DepartmentID': 1}
    getdicReState(actualValue, conditionR)
