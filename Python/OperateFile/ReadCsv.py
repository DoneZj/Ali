def ReadCsv(path):
    context=''
    try:
        with open(path,encoding='utf-8') as f:
            context = f.readlines()
    except(IOError):
        print('文件路径['+path+']有问题,该文件无法打开!')
    finally:
        f.close()
        return context




