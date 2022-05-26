import sys
import socket
import json
import ipaddress
from common.data_values import DEFAULT_ENCODING, DEFAULT_LIMIT_MESSAGE

def check_argv():
    script_name = sys.argv[0]
    script_name = script_name.split("/")
    if len(sys.argv) < 2:
        print(f"""Неверные аргументы! 
                 Пример использования {script_name[-1]} -a 127.0.0.1 -p 5555
                 где -a <АДРЕС СЕРВЕРА> -p <ПОРТ СЕРВЕРА>""")
        sys.exit()
    if sys.argv[1] != "-a" or sys.argv[3] != "-p":
            print(f"""Неверные аргументы! 
                     Пример использования {script_name[-1]} -a 127.0.0.1 -p 5555
                     где -a <АДРЕС СЕРВЕРА> -p <ПОРТ СЕРВЕРА>""")
    try:
        ipaddress.ip_address(sys.argv[2])
    except:
        print("Указан неправильный IP адрес", sys.argv[2])

    try:
        port = int(sys.argv[4])
        if port > 65535:
            raise TypeError
    except ValueError:
        print("Порт должен быть числом!")
    except TypeError:
        print("Порт должен быть в диапазоне от 1 до 65535")

    while True:
            print("Использовать параметры по умолчанию? (Да/Нет)(Y/N): ")
            answer = input()
            if answer.lower() == "да" or answer.lower() == "y":
                use_default_data = 1
                return use_default_data
            if answer.lower() == "нет" or answer.lower() == "n":
                sys.exit()



def get_message(client):
    encoded_response = client.recv(DEFAULT_LIMIT_MESSAGE)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(DEFAULT_ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError

def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(DEFAULT_ENCODING)
    sock.send(encoded_message)



