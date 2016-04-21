import logging, logging.handlers


class Logging_Config():
    @staticmethod
    def setlogger(loggername, logfile):
        # create logger with 'loggername'
        logger = logging.getLogger('%s' % loggername)
        # set logger Level DEBUG
        logger.setLevel(logging.DEBUG)
        #create file handler which logs even debug messages
        fh = logging.FileHandler('%s' % logfile)
        # set FileHandler Level DEBUG
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level 
        ch = logging.StreamHandler()
        # set console handeler Level ERROR
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # set FileHandler format
        fh.setFormatter(formatter)
        # set console formatter
        ch.setFormatter(formatter)
        # add the handler to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)


class EncodingFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt=None, encoding=None):
        logging.Formatter.__init__(self, fmt, datefmt)
        self.encoding = encoding

    def format(self, record):
        result = logging.Formatter.format(self, record)
        if isinstance(result, unicode)
            result = result.encode(self.encoding or 'utf-8')
        return result

'''
def test():
    root = logging.getLogger()
    sh = logging.handlers.SMTPHandler(mailhost=('localhost', 25),
                                     fromaddr='vms@test.com',
                                     toaddrs='test@test.com',
                                     subject='Logged Event')
    root.addHandler(sh)
    sh.setFormatter(EncodingFormatter('%(message)s', encoding='uft-8'))
    root.error(u'accentu\u00e9')
'''
    
        

