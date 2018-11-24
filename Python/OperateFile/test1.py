from os import path
import os
from Ali.Python.VelocityUtil.CustomExpection import RuntimeException

def getSpecificTestContent():
    parent_path = os.path.dirname(os.path.dirname(path.dirname(__file__)))  # 获得d所在的目录,即d的父级目录
    SPECIFIC_LIST_FILE = parent_path+r'/resoure/testcase/specificTest.list'
    # print(path)
    with open(SPECIFIC_LIST_FILE,encoding='utf-8') as f:
        content = f.readlines()
    # print('content=', content, type(content))
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
            Availablelist = line.strip('\n')
            print('Availablelist=',Availablelist)
        # execute(x)

allFileNum = 0
def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    print('子目录',files)
    # print('files=',files)
    # 先添加目录级别
    dirList.append(str(level))

    for f in files:
        # print('f=',f)
        if (os.path.isdir(path + '/' + f)):
            path1 = (path + '\\' + f)
            print('下一级目录:',path1)
    #         # with open(path1,encoding='utf-8') as f:
    #         #     a =f.readlines()
    #         #     print(a)
    #         # 排除隐藏文件夹。因为隐藏文件夹过多
    #         if (f[0] == '.'):
    #             pass
    #         else:
    #             # 添加非隐藏文件夹
    #             dirList.append(f)
    #     if (os.path.isfile(path + '/' + f)):
    #         # 添加文件
    #         fileList.append(f)
    #         # 当一个标志使用，文件夹列表第一个级别不打印
    # i_dl = 0
    # for dl in dirList:
    #     if (i_dl == 0):
    #         i_dl = i_dl + 1
    #     else:
    #         # 打印至控制台，不是第一个的目录
    #         # print('TEST下的dl目录:', dl)
    #         # print('-' * (int(dirList[0])), dl)
    #         # 打印目录下的所有文件夹和文件，目录级别+1
    #         printPath((int(dirList[0]) + 1), path + '/' + dl)
    # for fl in fileList:
    #     pass
    #     # 打印文件
    #     # print("最终文件", fl)
    #     # 随便计算一下有多少个文件
    #     allFileNum = allFileNum + 1


    # print('dirList=',dirList)
    # print('fileList=', fileList)


if __name__ == '__main__':
    # getSpecificTestContent()
    printPath(1,r'C:\Users\ZhangJ\PycharmProjects\untitled\Ali')
    # print('总文件数 =', allFileNum)