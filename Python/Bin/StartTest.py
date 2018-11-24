
from Python.DBCheck.DBCHECKByCsv import DBCheckByCsv
from Python.OperateFile.LoadFiles import getSpecificTestContent
from Python.VelocityUtil.CustomExpection import RuntimeException


def main1():
    testcontex = {'refundAmountValue': 12345, 'instructionId': 'vuales1', 'depositId': 76975754745710}
    path = r"C:\Users\ZhangJ\PycharmProjects\untitled\Ali\Python\File\DBSys_UserInfo.csv"
    dbcheckbycsv = DBCheckByCsv(path, testcontex)
    dbcheckbycsv.DBCheck()
    dbcheckbycsv.DBCheck(2)
    dbcheckbycsv.DBCheck(3)

def main():
    Availablelist = getSpecificTestContent()
    if len(Availablelist)<=0:
        raise RuntimeException('SPECIFIC_LIST_FILE is not found or file is empty!')
    else:
        for test in Availablelist:
            # execute(test)
            print(test)

if __name__ == '__main__':
    main1()