from Python.DBCheck.getVariablevalue import getVariableValueDic
from Python.OperateFile.ReadCsv import ReadCsv
from Python.VelocityUtil.Judgment import isDicContainKey


class GetCsvContextForDbcheck:
    '通过读取Csv文件校验数据库'
    def __init__(self,path,index,testcontex):
        '''
        :param path: csv文件的路径
        :param index: 需要校验的列
        :param testcontex: 测试上下文，全局变量
        '''
        self.path = path
        self.index = index
        self.testcontex = testcontex
        self.all = []
        # 需要查询的列(列表类型)
        self.selectcolums = []
        # where条件列(字典类型)
        self.conditionC = {}
        # 需要dbcheck的列(字典类型)
        self.conditionY = {}
        # 需要正则的列(字典类型)
        self.conditionR = {}

    def getCsvContextByFlag(self):
        '通过flag标识来读取csv文件内容'
        # 读取CSV文件
        context = ReadCsv(self.path)
        # print('context=',context)

        # 循环读取的内容,得到各种条件的值
        for i in range(len(context)):
            # 去掉空和换行符，并使用逗号隔开
            ervery = context[i].replace(" ", "").replace("\n", "").split(',')
            self.all.append(ervery)
            # erveryline = context[i].replace(" ","").replace("\n","").split(',')
            # ervery = self.getVariableValue(erveryline,self.testcontex)
            # 默认查询所有的列,数据量大速度慢
            # selectcolums.append(ervery[1])
            # 默认查询需要校验或正则(flag=Y或者flag=R)的条件
            if (ervery[3].upper() == 'Y' or ervery[3] == 'R') and i > 0:
                self.selectcolums.append(ervery[1])
            # 获取所有的where条件的字段并加入对应的字典中
            if ervery[3].upper() == 'C' and i > 0:
                self.conditionC[ervery[1]] = ervery[3+self.index]
            # 获取所有的需要校验校验的字段并加入对应的字典中
            if ervery[3].upper() == 'Y' and i > 0:
                self.conditionY[ervery[1]] = ervery[3+self.index]
            # 获取所有的需要正则校验的字段并加入对应的字典中
            if ervery[3].upper() == 'R' and i > 0:
                self.conditionR[ervery[1]] = ervery[3+self.index]
            # 判断重写N部分(后面expect中可以重写定义是否不需要校验),N:不处理,Y:校验，R:正则，C:条件
            if type(ervery[3 + self.index]) == str and (
                ervery[3 + self.index].startswith('N|') or ervery[3 + self.index].startswith('n|')):
                columN = ervery[1]
                if isDicContainKey(columN, self.conditionC):
                    self.conditionC.pop(columN)
                elif isDicContainKey(columN, self.conditionR):
                    self.conditionR.pop(columN)
                elif isDicContainKey(columN, self.conditionY):
                    self.conditionY.pop(columN)
                # 若之前的部分在需要查询的列list(selectcolums)中，则此处进行删除操作。也可不进行删除
                if columN in self.selectcolums:
                    self.selectcolums.remove(columN)
        self.tablename = self.all[1][0].lower()

    def getCsvContextByExp(self):
        '通过exp来读取csv文件内容,部分字段需要更改状态'
        # 读取CSV文件
        context = ReadCsv(self.path)
        for i in range(len(context)):
            # 去掉空和换行符，并使用逗号隔开
            ervery = context[i].replace(" ", "").replace("\n", "").split(',')
            # 判断重写C部分(后面expect中可以重写定义是否作为查询条件),N:不处理,Y:校验，R:正则，C:条件
            if type(ervery[3 + self.index]) == str and (
                ervery[3 + self.index].startswith('C|') or ervery[3 + self.index].startswith('c|')):
                columC = ervery[1]
                if isDicContainKey(columC, self.conditionR):
                    self.conditionR.pop(columC)
                elif isDicContainKey(columC, self.conditionY):
                    self.conditionY.pop(columC)
                elif columC not in self.selectcolums:
                    self.selectcolums.append(columC)
                # 将需要C的部分条件到conditionC字典中
                self.conditionC[columC] = ervery[3 + self.index].split('|')[1]
            # 判断重写Y部分(后面expect中可以重写定义是否需要校验),N:不处理,Y:校验，R:正则，C:条件
            if type(ervery[3 + self.index]) == str and (
                ervery[3 + self.index].startswith('Y|') or ervery[3 + self.index].startswith('y|')):
                columY = ervery[1]
                if isDicContainKey(columY, self.conditionR):
                    self.conditionR.pop(columY)
                elif isDicContainKey(columY, self.conditionC):
                    self.conditionC.pop(columY)
                elif columY not in self.selectcolums:
                    self.selectcolums.append(columY)
                # 将需要Y的部分条件到conditionY字典中
                self.conditionY[columY] = ervery[3 + self.index].split('|')[1]
            # 判断重写R部分(后面expect中可以重写定义是否需要正则),N:不处理,Y:校验，R:正则，C:条件
            if type(ervery[3 + self.index]) == str and (
                ervery[3 + self.index].startswith('R|') or ervery[3 + self.index].startswith('r|')):
                columR = ervery[1]
                if isDicContainKey(columR, self.conditionY):
                    self.conditionY.pop(columR)
                elif isDicContainKey(columR, self.conditionC):
                    self.conditionC.pop(columR)
                elif columR not in self.selectcolums:
                    self.selectcolums.append(columR)
                # 将需要R的部分条件到conditionR字典中
                self.conditionR[columR] = ervery[3 + self.index].split('|')[1]
        self.conditionC = getVariableValueDic(self.testcontex, self.conditionC)
        self.conditionY = getVariableValueDic(self.testcontex, self.conditionY)
        self.conditionR = getVariableValueDic(self.testcontex, self.conditionR)
        # print("conditionC=",self.conditionC)
        # print("selectcolums=",self.selectcolums)
        # print("conditionR=",self.conditionR)
        # print("conditionY=",self.conditionY)

    def getAllInfo(self):
        '获取完整的csv文件内容'
        self.getCsvContextByFlag()
        self.getCsvContextByExp()
if __name__ == '__main__':
    testcontex = {'refundAmountValue': 12345, 'instructionId': 'vuales1', 'depositId': 76975754745710}
    path =r"C:\Users\ZhangJ\PycharmProjects\untitled\Ali\Python\File\DBSys_UserInfo.csv"
    getCsvContextForDbcheck = GetCsvContextForDbcheck(path,2,testcontex)
    getCsvContextForDbcheck.getAllInfo()
    all = getCsvContextForDbcheck.all
    print('all=',all)
    tablename = getCsvContextForDbcheck.tablename
    print('tablename=',tablename)
    selectcolums = getCsvContextForDbcheck.selectcolums
    print('selectcolums=',selectcolums)
    conditionC = getCsvContextForDbcheck.conditionC
    print('conditionC=',conditionC)
    conditionY = getCsvContextForDbcheck.conditionY
    print('conditionY=',conditionY)
    conditionR = getCsvContextForDbcheck.conditionR
    print('conditionR=',conditionR)

