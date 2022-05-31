import json
import socket
import time
import sys
import logging
from common.data_values import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_SERVER_ADR, DEFAULT_SERVER_PORT
from common.data_function import get_message, send_message, check_argv
import logmydata.config_log_client


CLIENT_LOGGER = logging.getLogger('client')


def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name} c временем {time.time()}')
    return out


def process_ans(message):

    if RESPONSE in message:
        CLIENT_LOGGER.debug(f'Разбор сообщения от сервера')
        if message[RESPONSE] == 200:
            CLIENT_LOGGER.debug(f'Сообщение со статусом 200 - OK')
            return '200 : OK'
        CLIENT_LOGGER.debug(f'Сообщение со статусом 400 - NOT OK')
        return f'400 : {message[ERROR]}'
    raise ValueError(CLIENT_LOGGER.debug(f'Ошибка в функции process_ans() {ValueError}'))



def main():
    check_argv()
    server_address = DEFAULT_SERVER_ADR
    server_port = DEFAULT_SERVER_PORT
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')
        CLIENT_LOGGER.info(f'Не удалось декодировать полученную Json строку {ValueError}')
    transport.shutdown(socket.SHUT_RDWR)
    transport.close()


if __name__ == '__main__':
    main()
