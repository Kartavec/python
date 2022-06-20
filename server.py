import socket
import json
import sys
import logging
from common import data_values
from common import data_function
from common.data_function import get_message, send_message
from common.data_values import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
import logmydata.config_log_server
from logmydata.decorator_log import log


SERVER_LOGGER = logging.getLogger('server')

@log
def process_client_message(message):
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        SERVER_LOGGER.debug(f'Статус : 200 - OK')
        return {RESPONSE: 200}
    SERVER_LOGGER.debug(f'Статус : 400 - BAD')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    use_default_data = data_function.check_argv()
    if use_default_data == 1:
        server_addr = data_values.DEFAULT_SERVER_ADR
        server_port = data_values.DEFAULT_SERVER_PORT
    else:
        server_addr = sys.argv[2]
        server_port = sys.argv[4]
    SERVER_LOGGER.debug(f'Сервер будет запущен на {server_addr} Порт {server_port}')

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((server_addr, server_port))
    transport.listen(data_values.DEFAULT_MAX_CLIENTS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соедение с {client} {client_address}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.info(f'Сообщение от клиента - {message_from_client}')
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
            SERVER_LOGGER.info(f'ЗАКРЫТО установленое соедение с {client} {client_address}')
        except (ValueError, json.JSONDecodeError):
            SERVER_LOGGER.error(f'Ошибка {ValueError} , сообщение от клиента')
            client.close()


main()
