#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: PrintTable.py
@time: 2018-08-25 21:09
@desc:
'''
import prettytable as pt
from prettytable import *

from Python.VelocityUtil.Logging import Logger


def PrintTable():
    log = Logger().logger
    '添加行'
    # 按行添加数据
    tb = pt.PrettyTable()
    # 设定左对齐
    tb.align = 'l'
    # 设定显示所有分割线
    tb._set_hrules(ALL)
    tb.field_names = ["TableName", "Column", "Flag", "ActualValue"," Exp","Result"]
    return  tb

def PrintDBCheckResult(resultY,resultR,tb,tablename):
    log = Logger(style = 'DBcheck').logger
    '打印最终的结果'
    if len(resultY) > 0 and len(resultR) > 0:
        # print('A')
        for index in range(len(resultY)):
            tb.add_row([tablename, resultY[index][0], "Y", resultY[index][1], resultY[index][2], False])
        for index in range(len(resultR)):
            tb.add_row([tablename, resultR[index][0], "R", resultR[index][1], resultR[index][2], False])
        log.debug(tb)
        raise AssertionError("[Column=%s]:actualValue(%s) != expectvalue(%s)" % (resultY[0][0], resultY[0][1],
                                                                                 resultY[0][2]))
    elif len(resultY) > 0:
        # print('B')
        for index in range(len(resultY)):
            tb.add_row([tablename, resultY[index][0], "Y", resultY[index][1], resultY[index][2], False])
        log.debug(tb)
        raise AssertionError(
            "[Column=%s]:actualValue(%s) != expectvalue(%s)" % (resultY[0][0], resultY[0][1], resultY[0][2]))
    elif len(resultR) > 0:
        # print('C')
        for index in range(len(resultR)):
            tb.add_row([tablename, resultR[index][0], "R", resultR[index][1], resultR[index][2], False])
        log.debug(tb)
        raise AssertionError(
            "[Column=%s]:actualValue(%s) != expectvalue(%s)" % (resultR[0][0], resultR[0][1], resultR[0][2]))
    else:
        # print('D')
        log.debug(tb)
