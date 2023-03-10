import logging
from config import settings


logging.basicConfig(level=settings.LOG_LEVEL)
log = logging.getLogger()
log.info("Logging configuration set")
