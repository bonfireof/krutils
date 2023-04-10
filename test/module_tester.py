import KRLog


logger = KRLog.logger(__file__)


a = 10.0

logger.syslog("[%%]", a)
logger.dblog("[%%]", a)
logger.debug("[%%]", a)
logger.info("[%%]", a)
logger.error("[%%]", a)


