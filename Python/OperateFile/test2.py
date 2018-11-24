import os
from os import path

def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)

parent_path = os.path.dirname(os.path.dirname(path.dirname(__file__)))  # 获得d所在的目录,即d的父级目录
print('parent_path=',parent_path)
list1=[]
dir = listdir(parent_path,list1)
print('list1=',list1)
print('len=',len(list1))
for x in list1:
    if x.endswith('.py'):
        print('-' * 10 + x + '-' * 10)
        with open(x,encoding="utf-8") as f:
            context = f.read()
        f.close()
        print(context)
