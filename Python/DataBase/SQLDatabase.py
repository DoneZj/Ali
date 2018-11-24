import pymssql
import time
from Python.VelocityUtil.CustomExpection import NullException
from Python.VelocityUtil.Logging import Logger

class sqlDatabase:
    def __init__(self,host,user,password,database,port=1433,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.log = Logger().logger
    def SqlConnet(self):
        self.connect = pymssql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
        self.cursor = self.connect.cursor()

    def SqlClose(self):
        self.connect.close()

    #定义装饰器，若查询数据库返回值为Null(数据库中无数据)，则默认查询times(times=3)次,每次间隔sleeptime秒
    def retry(times=3,sleeptime=3, exceptions=None):
        exceptions = exceptions if exceptions is not None else Exception
        def wrapper(func):
            def wrapper(*args, **kwargs):
                log = Logger().logger
                last_exception = None
                for _ in range(times):
                    try:
                        log.debug('Sleeptime=%sS' % (sleeptime))
                        time.sleep(sleeptime)
                        return func(*args, **kwargs)
                    except exceptions as e:
                        last_exception = e
                raise last_exception
            return wrapper
        return wrapper
    @retry()
    def SqlQuery(self, sqlcontext,tablename):
        self.log.info('执行SQL:[%s]' % (sqlcontext))
        self.cursor.execute(sqlcontext)
        # 返回结果(元组)
        datas = self.cursor.fetchall()
        if len(datas) > 0:
            self.SqlClose()
            return datas
        else:
            raise NullException("执行SQL:[%s],返回结果为Null;数据源:[%s],数据表:[%s]"%(sqlcontext,self.database,tablename))



if __name__ == '__main__':
    sqldata = sqlDatabase('127.0.0.1','sa','1234','WEBUIS_YS')
    sqlcontext = "select UserInfoID,HospitalID,DepartmentID,LoginName,Password,UserName,Sex,UserType,StartDate,EndDate,State from sys_userinfo where UserInfoID='4' and JobNumber='10580'"
    sqldata.SqlConnet()
    data = sqldata.SqlQuery(sqlcontext,'WEBUIS_YS_sys')
    print(data)