from src.framework.logger import Logger

logger = Logger('test').getlog()
logger.debug('debug 信息')
logger.warning('只有这个会输出。。。')
logger.info('info 信息')