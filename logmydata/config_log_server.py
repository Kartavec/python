import sys
import os
import logging
import logging.handlers
from common.data_values import DEFAULT_LOGGING_LEVEL, DEFAULT_LOGFILENAME_SERVER


SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')


PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, DEFAULT_LOGFILENAME_SERVER)

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)


LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(DEFAULT_LOGGING_LEVEL)
