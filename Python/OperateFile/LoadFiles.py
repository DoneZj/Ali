import os
import threading
from os import path

from Python.VelocityUtil.CustomExpection import RuntimeException
from Python.VelocityUtil.Logging import Logger

log = Logger().logger
def listdir(path,list_name):  #传入存储的list
    '加载所有文件的路径'
    """
    path:需要读取的路径
    list_name:path目录下的所有路径的list
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)

def readpyfile(path):
    '读取所有以.py结尾的文件，并返回对应的内容'
    if path.endswith('.py'):
        with open(path,encoding="utf-8") as f:
            context = f.read()
        f.close()
        return  context

def threadingfun(lists,fun):
    '多线程读取文件列表'
    threadl = []
    for listElement in lists:
        thread = threading.Thread(target=fun, args=(listElement,))
        log.debug('Load:'+r'%s',listElement)
        threadl.append(thread)
        thread.start()
    for thread in threadl:
        thread.join()
    log.debug("线程读取文件完成！")

def getSpecificTestContent():
    parent_path = os.path.dirname(os.path.dirname(path.dirname(__file__)))  # 获得d所在的目录,即d的父级目录
    SPECIFIC_LIST_FILE = parent_path+r'/resoure/testcase/specificTest.list'
    Availablelist=[]
    with open(SPECIFIC_LIST_FILE,encoding='utf-8') as f:
        content = f.readlines()
    if len(content) == 0:
        raise RuntimeException('['+SPECIFIC_LIST_FILE + "] is not found or file is empty!")
    for line in content:
        #去掉以'#'开头不可用的
        if line.startswith('#'):
            continue
        # 去掉以'\n'换行符
        elif line.startswith('\n'):
            continue
        else:
            # 去掉行尾换行符'\n'
            Availablelist.append(line.strip('\n'))
    return Availablelist



