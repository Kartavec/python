#!/usr/local/bin/python

import yaml
import socket
import json
import logging
from argparse import ArgumentParser
from actions import resolve
from protocol import validate_request, make_response

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file')

args = parser.parse_args()

host = 'localhost'
port = 8000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader = yaml.Loader)
        host = config.get('host')
        port = config.get('port')

logger = logging.getLogger('mail')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('main.log') #encoding

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

print(f'Client run on {host}:{port}')
data = input('Enter data: ')
print(data)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    logger.info(f'Server was started on {host}:{port}')

    while True:
        client, address = sock.accept()
        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    logger.critical(err)
                    response = make_response(request, 500, 'Internal server error')
            else:
                logger.error(f'404 - request: {request}')
                response = make_response(request, 404, 'Action not found')
        else:
            logger.error(f'400 - request: {request}')
            response = make_response(request, 400, 'Wrong request')
        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))
        client.close()
except KeyboardInterrupt:
    pass

