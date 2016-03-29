#-*-coding:utf8-*-

from datetime import datetime
import logging
class LogTool(object):
    def __init__(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename = 'logs\\'+datetime.now().strftime('%Y%m%d%H%M%S')+ '.log',
            filemode='a'
        )
    def writeLog(self, logContent):
        logging.info(logContent)

    def writeErrorLog(self, errorContent):
        logging.error(errorContent)