import os
import sys
import logging
sys.path.append(os.path.join(os.getcwd(), '..'))
import logmydata.config_log_client
import logmydata.config_log_server


def log(function):

    def log_saver(*args, **kwargs):
        logger_name = 'server' if 'server.py' in sys.argv[0] else 'client'
        LOGGER = logging.getLogger(logger_name)

        ret = function(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {function.__name__} c параметрами {args}, {kwargs}.'
                     f'Вызов из модуля {function.__module__}.')
        return ret

    return log_saver