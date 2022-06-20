import sys
import os
import logging
import logging.handlers
from common.data_values import DEFAULT_LOGGING_LEVEL, DEFAULT_LOGFILENAME_SERVER


SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

temm = os.path.abspath(os.path.join(__file__, ".."))
temm = os.path.dirname(temm)
PATH = os.path.join(temm, "logs", f'{DEFAULT_LOGFILENAME_SERVER}')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)


LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(DEFAULT_LOGGING_LEVEL)
