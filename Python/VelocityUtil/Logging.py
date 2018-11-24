import logging
from logging import handlers
import time

class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self,filename='../File/Testlog_'+time.strftime('%Y-%m-%d',time.localtime()) +'.log',level='debug',when='D',backCount=3,style='NoDBcheck'):
        fmt = '%(asctime)s - %(levelname)s:%(funcName)s[%(lineno)d], %(message)s'
        if style == 'DBcheck':
            fmt = '%(asctime)s - %(levelname)s:%(funcName)s[%(lineno)d]:\n%(message)s'
        self.logger = logging.getLogger(filename)
        # 判断logger是否已经添加过handler，是则直接返回logger对象，否则执行handler设定以及addHandler(ch)
        if  self.logger.handlers:
            self.logger.handlers.clear()
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        # interval 是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

if __name__ == '__main__':
    # time.strftime('%Y_%m_%d',time.localtime()) +
    log = Logger()
    log.logger.debug('uioyoi')
    log.logger.info('uioyoi')
