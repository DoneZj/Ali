import traceback

from Python.VelocityUtil.Logging import Logger


class AssertUtil():
    def __init__(self):
        self.log = Logger().logger

    def assertDic(self,actualdic,expectdic,tb,tablename):
        if type(actualdic) == dict and type(expectdic) == dict and (len(actualdic)>=len(expectdic)):
            res = []
            for expectdickey in expectdic:
                expectvalue = str(expectdic[expectdickey])
                actualvalue = str(actualdic[expectdickey])
                # self.log.debug('%s: expectvalue=%s,actualvalue=%s'%(expectdickey,expectvalue,actualvalue))
                # self.assertEqual(actualvalue,expectvalue,'%s实际值和期望值不等,actualvalue=%s;expectdickey=%s'%(expectdickey,actualvalue,expectdickey))
                try:
                    assert actualvalue == expectvalue
                    tb.add_row([tablename,expectdickey,"Y",actualvalue,expectvalue,True])
                except AssertionError as e:
                    self.log.debug(traceback.format_exc()+ 'AssertionError:[Column=%s(Flag=Y)]:actualValue(%s) != expectvalue(%s)' % (
                        expectdickey, actualvalue, expectvalue))
                    res.append([expectdickey,actualvalue, expectvalue])
                    continue
            return  res
        else:
            return False
