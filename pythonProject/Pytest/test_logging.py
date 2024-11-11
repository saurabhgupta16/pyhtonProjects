import logging
#debug
#info
#warning
#error
#Critical
def test_loggingdemo():

    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.ERROR)
    logger.debug("i am in debug mode")
    logger.info("i am in info mode")
    logger.warning("i am in warning mode")
    logger.error("i am in error mode")
    logger.critical("i am in critical mode")
