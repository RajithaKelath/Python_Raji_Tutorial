from logging import basicConfig, getLogger

basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)-2d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S' ,
    level='DEBUG',
    filename='test.log')
logger = getLogger('__name__')

logger.debug("This is debug message")
logger.critical("This is critical message")
logger.error("This is error message")
logger.info("This is info message")
logger.warning("This is warning message")