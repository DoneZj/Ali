import sys
from Python.DBCheck.GetCsvContextForDbcheck import GetCsvContextForDbcheck
from Python.DBCheck.PrintTable import PrintTable, PrintDBCheckResult
from Python.DBCheck.getVariablevalue import getvaluefromDic
from Python.DataBase.SQLDatabase import sqlDatabase
from Python.VelocityUtil.AssembleStructure import dicAnd
from Python.VelocityUtil.AssertUtil import AssertUtil
from Python.VelocityUtil.Logging import Logger
from Python.VelocityUtil.TypeConvert import tuplelistToDic
from Python.VelocityUtil.getValueforRe import getdicReState


sys.stderr = sys.stdout
class DBCheckByCsv():
    '通过读取Csv文件来进行DBCheck'
    def __init__(self,path,testcontex):
        '''
        :param index: 需要校验的Exp的第几列
        :param path: Csv文件路径
        :param testcontex: 测试上下文，全局变量，字典类型
        '''
        self.log = Logger().logger
        self.path = path
        self.testcontex = testcontex

    def DBCheck(self,index=1):
        self.log.debug('开始执行DBCheck,Csv路径:%s;[Index=%s]'%(self.path,index))
        getCsvContextForDbcheck = GetCsvContextForDbcheck(self.path, index, self.testcontex)
        getCsvContextForDbcheck.getAllInfo()
        all = getCsvContextForDbcheck.all
        tablename = getCsvContextForDbcheck.tablename
        # self.log.debug('DBCheck Info:tablename=%s'%tablename)
        # self.log.debug('DBCheck Info:all=%s' % all)
        selectcolums = getCsvContextForDbcheck.selectcolums
        # self.log.debug('DBCheck Info:selectcolums=%s' % selectcolums)
        conditionC = getCsvContextForDbcheck.conditionC
        # self.log.debug('DBCheck Info:conditionC=%s' % conditionC)
        conditionY = getCsvContextForDbcheck.conditionY
        # self.log.debug('DBCheck Info:conditionY=%s' % conditionY)
        conditionR = getCsvContextForDbcheck.conditionR
        # self.log.debug('DBCheck Info:conditionR=%s'%conditionR)

        # 拼装where条件语句
        wherecondition = dicAnd(conditionC)
        # 拼装SQL语句
        sqlcontent = 'select ' + ",".join(selectcolums) + ' from ' + tablename + ' where ' + wherecondition
        # 连接数据库
        sqldatabase = sqlDatabase('127.0.0.1','sa','1234','WEBUIS_YS')
        sqldatabase.SqlConnet()
        # 查询获取数据库
        getdatas = sqldatabase.SqlQuery(sqlcontent,tablename)
        # self.log.debug('DBCheck QueryResult List:%s' % getdatas)
        # 获取实际值,将getdatas(List类型)转成对应的dic类型
        actualValue = tuplelistToDic(selectcolums, getdatas)
        # self.log.debug('DBCheck actualValue(QueryResult Dict):%s' % actualValue)

        #准备打印DBCheck表格
        tb = PrintTable()
        #将where条件(conditionC)add到表格中
        getvaluefromDic(conditionC,tb,tablename)
        # 断言期望值Y
        assertUtil = AssertUtil()
        resultY = assertUtil.assertDic(actualValue,conditionY,tb,tablename)
        # 获取查询结果R(正则)之后得到实际值
        resultR = getdicReState(actualValue, conditionR, tablename, tb)
        #打印最终的DBCheck的结果
        PrintDBCheckResult(resultY,resultR,tb,tablename)

if __name__ == '__main__':
    testcontex = {'refundAmountValue': 12345, 'instructionId': 'vuales1','depositId':76975754745710}
    path = r"C:\Users\ZhangJ\PycharmProjects\untitled\Ali\Python\File\DBSys_UserInfo.csv"
    dbcheckbycsv = DBCheckByCsv(path,testcontex)
    dbcheckbycsv.DBCheck()
    dbcheckbycsv.DBCheck(2)
    dbcheckbycsv.DBCheck(3)