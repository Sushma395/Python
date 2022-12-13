import inspect
import logging


class BaseClass:
    def getLogger(self):

        # logger = logging.getLogger(__name__)
        # to get child class name isntead of base class in demo 5, need to create variable and pass it to getLogger
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler = logging.FileHandler('logfile1.log')  # file for logging
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        #logger.setLevel(logging.CRITICAL)
        logger.setLevel(logging.DEBUG)

        return logger
