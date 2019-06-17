import logging
from functools import wraps
from protocol import make_response

logger = logging.getLogger('decorators')


def logger_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.debug(f'{func.__name__} : {request}')
        return func(request, *args, ** kwargs)
    return wrapper

def login_required(func): #проверка пользователя а стороне сервера
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if 'user' in request:
            return func(request, *args, **kwargs)
        return make_response(request, 403,'Access denied')
    return wrapper()