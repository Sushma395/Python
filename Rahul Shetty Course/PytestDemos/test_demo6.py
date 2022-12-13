import logging


def test_logging():
    logger = logging.getLogger(__name__)  # __name__ will extract test case name

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    # name is test case name, levelname is type of log to be printed
    filehandler = logging.FileHandler('logfile.log')  # file for logging
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  # filehandler object

    logger.setLevel(logging.INFO)  # to set levelname

    # hierarchy of logging in asc
    # if level is set to warning, logger will print from warning till last level(critical) only
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Warning message")
    logger.error("Test got failed")
    logger.critical("Critical issue")
